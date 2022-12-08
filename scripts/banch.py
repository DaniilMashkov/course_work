from main.get_by_date import get_by_date
import re
from functools import cache


def input_args():
    args = {}

    dt = input('Дата в формате yyyy-mm-dd [all]: \n')
    if re.findall(r'[20]\d\d[-][0-1]\d[-][0-3]\d', dt):
        args['date'] = dt
    else:
        print('Неверный формат даты, будут выведены данные за всё время\n')

    tk = input('Тикер [all]: \n').upper()
    args['name'] = tk

    file = input('Файл [dump.csv]: \n')
    if re.findall(r'\w+.csv', file):
        args['filename'] = file
    else:
        args['filename'] = 'dump.csv'
        print('Введено некорректное наименование, будет использовано значение по-умолчанию: dump.csv\n')

    return get_by_date(**args)
