import sys
from collections import defaultdict


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


# Вариант 2
def find_odd_even(num):
    """num - int"""
    spam = defaultdict(int)
    for n in str(num):
        if int(n) % 2 == 0:
            spam['even'] += 1
        else:
            spam['odd'] += 1

    print(f'Четных: {spam["even"]}\nНечетных: {spam["odd"]}')
    return locals()


print(show_size(find_odd_even(12345)))
"""
type = <class 'dict'>, size = 232, object = {'num': 12345, 'spam': defaultdict(<class 'int'>, {'odd': 3, 'even': 2}), 'n': '5'}
type = <class 'tuple'>, size = 56, object = ('num', 12345)
type = <class 'str'>, size = 52, object = num
type = <class 'int'>, size = 28, object = 12345
type = <class 'tuple'>, size = 56, object = ('spam', defaultdict(<class 'int'>, {'odd': 3, 'even': 2}))
type = <class 'str'>, size = 53, object = spam
type = <class 'collections.defaultdict'>, size = 240, object = defaultdict(<class 'int'>, {'odd': 3, 'even': 2})
type = <class 'tuple'>, size = 56, object = ('odd', 3)
type = <class 'str'>, size = 52, object = odd
type = <class 'int'>, size = 28, object = 3
type = <class 'tuple'>, size = 56, object = ('even', 2)
type = <class 'str'>, size = 53, object = even
type = <class 'int'>, size = 28, object = 2
type = <class 'tuple'>, size = 56, object = ('n', '5')
type = <class 'str'>, size = 50, object = n
type = <class 'str'>, size = 50, object = 5
"""

"""ВЫВОД: по потребленной памяти 1 вариант оказался оптимальным, 2й - на втором месте и третью позицию заняло 
последнее решение"""