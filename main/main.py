import pandas as pd
from main.funcs import sort_func, quick_sort, save_file


def select_sorted(**kwargs):
    df = pd.read_csv('data/all_stocks_5yr.csv', na_filter=False, dtype={1: str, 2: str, 3: str, 4: str})
    lst = df.to_dict('records')

    if kwargs.get('sort_columns'):
        """Здесь можно выбрать между встроенной функцией и собственной реализацией"""
        # lst = quick_sort(lst, kwargs)
        lst = sort_func(lst, kwargs)
    if kwargs.get('limit'):
        lst = lst[:kwargs['limit']]
    if kwargs.get('group_by_name'):
        lst = sorted(lst, key=lambda x: x['Name'])

    if kwargs.get('filename'):
        save_file(lst, f"data/{kwargs['filename']}", 'w')

    return lst
