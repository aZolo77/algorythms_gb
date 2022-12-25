import random
import timeit
import cProfile

"""Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
1) выбрать хорошую задачу, которую имеет смысл оценивать
2) написать 3 варианта кода (один у вас уже есть)
3) проанализировать 3 варианта и выбрать оптимальный
4) результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры)
5) написать общий вывод: какой из трёх вариантов лучше и почему"""

"""Примечание: для получения достоверных результатов при замере времени необходимо исключить/заменить функции 
print() и input() в анализируемом коде"""

# Решение: урок 3 задание 5:
"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
значения"""


# Вариант 1:
def find_max_negative_1(arr):
    min_el = -float('inf')
    el_pos = None

    for i, item in enumerate(arr):
        if min_el < item < 0:
            min_el = item
            el_pos = i

    return min_el, el_pos


# Вариант 2:
def find_max_negative_2(arr):
    new_list = [i for i in arr if i < 0]
    min_el = max(new_list)
    el_pos = arr.index(min_el)
    return min_el, el_pos


# Вариант 3:
def find_max_negative_3(arr):
    el_pos = 0
    idx = -1
    size = len(arr)
    while el_pos < (size - 1):
        if arr[el_pos] < 0 and idx == -1:
            idx = el_pos
        elif 0 > arr[el_pos] > arr[idx]:
            idx = el_pos

        el_pos += 1

    return arr[idx], idx


# Измерения:
list_1 = [random.randint(-20, 10) for _ in range(10)]
# print(timeit.timeit('find_max_negative_1(list_1)', globals=globals()))  # 0.9193095000000001
# print(timeit.timeit('find_max_negative_2(list_1)', globals=globals()))  # 0.8307947000000001
# print(timeit.timeit('find_max_negative_3(list_1)', globals=globals()))  # 1.4818365000000002

list_2 = [random.randint(-40, 10) for _ in range(50)]
# print(timeit.timeit('find_max_negative_1(list_2)', globals=globals()))  # 3.3289467999999998
# print(timeit.timeit('find_max_negative_2(list_2)', globals=globals()))  # 3.0084702
# print(timeit.timeit('find_max_negative_3(list_2)', globals=globals()))  # 6.959609199999999

list_3 = [random.randint(-100, 10) for _ in range(100)]
# print(timeit.timeit('find_max_negative_1(list_3)', globals=globals()))  # 5.0450634
# print(timeit.timeit('find_max_negative_2(list_3)', globals=globals()))  # 5.0543653
# print(timeit.timeit('find_max_negative_3(list_3)', globals=globals()))  # 15.548424100000002

list_4 = [random.randint(-100, 10) for _ in range(1000000)]
cProfile.run('find_max_negative_1(list_4)')
# 4 function calls in 0.049 seconds

cProfile.run('find_max_negative_2(list_4)')
# 7 function calls in 0.057 seconds

cProfile.run('find_max_negative_3(list_4)')
# 5 function calls in 0.163 seconds

"""Вывод: время выполнения функций по timeit и cPanel показал, что 3я функция работает дольше"""
