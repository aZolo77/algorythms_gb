"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы"""
import random

r_list = [random.randint(0, 20) for _ in range(20)]
print(r_list)

min_val = r_list[0]
max_val = r_list[0]
min_pos, max_pos = 0, 0

for i, item in enumerate(r_list):
    if item < min_val:
        min_val = item
        min_pos = i
    if item > max_val:
        max_val = item
        max_pos = i

r_list[min_pos] = max_val
r_list[max_pos] = min_val

print(r_list)
