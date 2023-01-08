import sys

# sys.version: 3.9.13
# sys.platform: [MSC v.1929 64 bit (AMD64)] win32


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
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


print(show_size(simple_odd_even_search(12345)))
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

"""ВЫВОД: по потребленной памяти 1 вариант оказался оптимальным, 2й - на втором месте и третью позицию заняло 
последнее решение"""
