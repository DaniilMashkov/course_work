from main.funcs import binary_search, save_file
import pandas as pd
import os


def get_by_date(**kwargs):
    data = pd.read_csv('data/all_stocks_5yr.csv', chunksize=100_000)

    for chunk in data:
        chunk = chunk.to_dict('records')
        if kwargs.get('date'):
            chunk = list(filter(lambda x: x['date'] == kwargs['date'], chunk))
        save_file(chunk, 'cache/filtered_chunk.csv', 'a')

    data = pd.read_csv('cache/filtered_chunk.csv', na_filter=False, dtype={1: str, 2: str, 3: str, 4: str})
    lst = data.to_dict('records')
    if lst:
        if kwargs.get('name'):
            lst.sort(key=lambda x: x['Name'])
            try:
                lst = [lst[binary_search(lst, kwargs['name'])]]
            except:
                print('Тикер не найден')
                lst = []
    else:
        lst = 'data/all_stocks_5yr.csv'

    save_file(lst, f'data/{kwargs["filename"]}', 'w')
    os.remove('cache/filtered_chunk.csv')
