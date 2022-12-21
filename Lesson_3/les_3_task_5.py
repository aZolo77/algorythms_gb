"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных
значения"""
import random

r_list = [random.randint(-20, 20) for _ in range(20)]
print(r_list)

min_el = -float('inf')
el_pos = None

for i, item in enumerate(r_list):
    if min_el < item < 0:
        min_el = item
        el_pos = i

print(f'Максимальный отрицательный элемент [{min_el}] в массиве находится по индексу: {el_pos}')
