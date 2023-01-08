import sys


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


# Вариант 3:
def odd_even_lst(num_str):
    """num - str"""
    odd_counter, even_counter = 0, 0
    num_lst = list(num_str)
    for n in num_lst:
        if int(n) % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1

    print(f'Четных: {even_counter}\nНечетных: {odd_counter}')
    return locals()


print(show_size(odd_even_lst('12345')))
"""
type = <class 'dict'>, size = 232, object = {'num_str': '12345', 'odd_counter': 3, 'even_counter': 2, 'num_lst': ['1', '2', '3', '4', '5'], 'n': '5'}
type = <class 'tuple'>, size = 56, object = ('num_str', '12345')
type = <class 'str'>, size = 56, object = num_str
type = <class 'str'>, size = 54, object = 12345
type = <class 'tuple'>, size = 56, object = ('odd_counter', 3)
type = <class 'str'>, size = 60, object = odd_counter
type = <class 'int'>, size = 28, object = 3
type = <class 'tuple'>, size = 56, object = ('even_counter', 2)
type = <class 'str'>, size = 61, object = even_counter
type = <class 'int'>, size = 28, object = 2
type = <class 'tuple'>, size = 56, object = ('num_lst', ['1', '2', '3', '4', '5'])
type = <class 'str'>, size = 56, object = num_lst
type = <class 'list'>, size = 96, object = ['1', '2', '3', '4', '5']
type = <class 'str'>, size = 50, object = 1
type = <class 'str'>, size = 50, object = 2
type = <class 'str'>, size = 50, object = 3
type = <class 'str'>, size = 50, object = 4
type = <class 'str'>, size = 50, object = 5
type = <class 'tuple'>, size = 56, object = ('n', '5')
type = <class 'str'>, size = 50, object = n
type = <class 'str'>, size = 50, object = 5
"""

"""ВЫВОД: по потребленной памяти 1 вариант оказался оптимальным, 2й - на втором месте и третью позицию заняло 
последнее решение"""

