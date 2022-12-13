"""Написать программу, которая генерирует в указанных пользователем границах:

a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от
'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно"""

import random

num = int(input('Выберите,что будет выведено:\n1 - целое число\n2 - вещественное число\n3 - буква\n'))

if num == 1:
    lower_bound = int(input('Нижняя граница: '))
    upper_bound = int(input('Верхняя граница: '))

    print(f'Случайное целое число: {random.randint(lower_bound, upper_bound)}')
elif num == 2:
    lower_bound = int(input('Нижняя граница: '))
    upper_bound = int(input('Верхняя граница: '))

    print(f'Случайное вещественное число: {random.uniform(lower_bound, upper_bound)}')
elif num == 3:
    start_sym = input('Символ 1: ')
    end_sym = input('Символ 2: ')

    start = ord(start_sym)
    end = ord(end_sym)

    random_num = random.randint(start, end)

    print(f'Случайный символ: {chr(random_num)}')
else:
    print('Неверно введено значение')
