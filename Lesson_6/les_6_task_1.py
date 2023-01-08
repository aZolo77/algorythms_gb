import sys
from collections import defaultdict

# sys.version: 3.9.13
# sys.platform: [MSC v.1929 64 bit (AMD64)] win32


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):  # коллекция
        if hasattr(x, 'items'):  # словарь
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


"""Lesson 2 Task 2: Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)"""


# Вариант 1:
def simple_odd_even_search(num):
    """num - int"""
    even, odd = 0, 0

    while num != 0:
        if num % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10

    print(f'Четных: {even}\nНечетных: {odd}')
    return locals()


# print(show_size(simple_odd_even_search(12345)))

"""
type = <class 'dict'>, size = 232, object = {'num': 0, 'even': 2, 'odd': 3}
type = <class 'tuple'>, size = 56, object = ('num', 0)
type = <class 'str'>, size = 52, object = num
type = <class 'int'>, size = 24, object = 0
type = <class 'tuple'>, size = 56, object = ('even', 2)
type = <class 'str'>, size = 53, object = even
type = <class 'int'>, size = 28, object = 2
type = <class 'tuple'>, size = 56, object = ('odd', 3)
type = <class 'str'>, size = 52, object = odd
type = <class 'int'>, size = 28, object = 3
"""


# Вариант 2:
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


# print(show_size(find_odd_even(12345)))

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


# print(show_size(odd_even_lst('12345')))

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
