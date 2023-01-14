"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

size = 15
arr = [round(random.uniform(0, 49), 2) for _ in range(size)]
random.shuffle(arr)

print(f'Список до сортировки:\n{arr}')


def merge_to_list(l, r):
    c = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            c.append(l[i])
            i += 1
        else:
            c.append(r[j])
            j += 1

    if i < len(l):
        c += l[i:]

    if j < len(r):
        c += r[j:]

    return c


def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    return merge_to_list(left, right)


print(f'Список после сортировки:\n{merge_sort(arr)}')
