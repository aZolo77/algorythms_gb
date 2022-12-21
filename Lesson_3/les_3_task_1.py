"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов"""
div_dict = dict.fromkeys(range(2, 10), 0)

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            div_dict[j] += 1

for key, item in div_dict.items():
    print(f'{key} кратны {item} числам')
