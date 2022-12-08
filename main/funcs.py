import csv


def quick_sort(lst, kwargs):
    """Реализовал quicksort вручную, работает очень медленно"""
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[1][kwargs['sort_columns'][0]]
        less = [i for i in lst[1:] if i[kwargs['sort_columns'][0]] and
                float(i[kwargs['sort_columns'][0]]) <= float(pivot)]
        greater = [i for i in lst[1:] if i[kwargs['sort_columns'][0]] and
                   float(i[kwargs['sort_columns'][0]]) > float(pivot)]
        if kwargs['order'] == 'asc':
            return quick_sort(less, kwargs) + quick_sort(greater, kwargs)
        else:
            return quick_sort(greater, kwargs) + quick_sort(less, kwargs)


def sort_func(lst, kwargs):
    return sorted(lst, key=lambda x:
    float(x[kwargs['sort_columns'][0]]) if x[kwargs['sort_columns'][0]] else 0,
                  reverse=True if kwargs['order'] == 'desc' else False)


def save_file(lst, filename, flag):
    with open(filename, flag, newline='') as file:
        fieldnames = lst[0].keys()
        write = csv.DictWriter(file, fieldnames)
        write.writeheader()
        [write.writerow(x) for x in lst]


def binary_search(lst, arg):
    low = 0
    high = len(lst)
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess['Name'] == arg:
            return mid
        if arg < guess['Name']:
            high = mid - 1
        else:
            low = mid + 1
    return None


