from main.main import select_sorted
import re


def input_args():
    sort_col = input(
        'Сортировать по цене: \nоткрытия (1) \nзакрытия (2) \nмаксимум [3] \nминимум (4) \nобъем (5) \n:'
        ' ')

    try:
        if int(sort_col) in (range(1, 6)):
            if sort_col == '3':
                sort_col = ['high']
            elif sort_col == '1':
                sort_col = ['open']
            elif sort_col == '2':
                sort_col = ['close']
            elif sort_col == '4':
                sort_col = ['low']
            elif sort_col == '5':
                sort_col = ['volume']
        else:
            sort_col = ['high']
            print('Введено некорректное значение, будет использовано значение по-умолчанию: 3\n')
    except:
        sort_col = ['high']
        print('Введено некорректное значение, будет использовано значение по-умолчанию: 3\n')

    acs_decs = input('Порядок по убыванию [1] / возрастанию (2):\n')
    try:
        if int(acs_decs) == 1:
            acs_decs = 'desc'
        if int(acs_decs) == 2:
            acs_decs = 'asc'
        else:
            acs_decs = 'desc'
            print('Введено некорректное значение, будет использовано значение по-умолчанию: 1\n')
    except:
        if acs_decs != 'desc':
            acs_decs = 'desc'
            print('Введено некорректное значение, будет использовано значение по-умолчанию: 1\n')

    lim = input('Ограничение выборки [10]:')
    try:
        if int(lim) in range(1, 1000000):
            lim = int(lim)
        else:
            lim = 10
            print('Введено некорректное значение, будет использовано значение по-умолчанию: 10\n')
    except:
        lim = 10
        print('Введено некорректное значение, будет использовано значение по-умолчанию: 10\n')

    file = input('Название файла для сохранения результата [dump.csv]: \n')
    if not re.findall(r'\w+.csv', file):
        file = 'dump.csv'
        print('Введено некорректное наименование, будет использовано значение по-умолчанию: dump.csv\n')

    args = {'sort_columns': sort_col, 'order': acs_decs, 'limit': lim, 'filename': file}
    return select_sorted(**args)
