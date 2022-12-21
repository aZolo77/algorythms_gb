"""Определить, какое число в массиве встречается чаще всего"""
import random

max_num = None
max_quantity = 0
r_list = [random.randint(0, 5) for _ in range(15)]
print(r_list)
print('*' * 30)

num_dict = {}

for item in r_list:
    if item in num_dict.keys():
        num_dict[item] += 1
    else:
        num_dict[item] = 1

print(num_dict)

for key, val in num_dict.items():
    if val > max_quantity:
        max_quantity = val
        max_num = key

print(f'Число [{max_num}] в случайном массиве встречается чаще всего (количество раз: {max_quantity})')
