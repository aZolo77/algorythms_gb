"""Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена»"""
import math
import timeit
import cProfile


def prime_counting_function(i):
    """Функция возвращает верхнюю границу отрезка на котором лежит i-e количество простых чисел"""

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


def eratostene_sieve(i):
    """Функция поиска i-го простого числа, используя алгоритм «Решето Эратосфена»"""

    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break

    return lst_prime[i - 1]


def sieve_without_eratostene(i):
    """Функция поиска i-го простого числа, без использования алгоритма «Решето Эратосфена»"""
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime[:]:
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


# Измерения:
print(timeit.timeit('eratostene_sieve(10)', number=1000, globals=globals()))  # 0.041304900000000005
print(timeit.timeit('eratostene_sieve(30)', number=1000, globals=globals()))  # 0.5861892
print(timeit.timeit('eratostene_sieve(60)', number=1000, globals=globals()))  # 2.5910017
print(timeit.timeit('eratostene_sieve(100)', number=1000, globals=globals()))  # 8.7961896

print(timeit.timeit('sieve_without_eratostene(10)', number=1000, globals=globals()))  # 0.007725100000000006
print(timeit.timeit('sieve_without_eratostene(30)', number=1000, globals=globals()))  # 0.0454972
print(timeit.timeit('sieve_without_eratostene(60)', number=1000, globals=globals()))  # 0.1642449
print(timeit.timeit('sieve_without_eratostene(100)', number=1000, globals=globals()))  # 0.4371511


cProfile.run('eratostene_sieve(10)')  # 87 function calls in 0.001 seconds
cProfile.run('eratostene_sieve(50)')  # 631 function calls in 0.002 seconds
cProfile.run('eratostene_sieve(100)')  # 1418 function calls in 0.009 seconds
cProfile.run('eratostene_sieve(500)')  # 8913 function calls in 0.503 seconds

cProfile.run('sieve_without_eratostene(10)')  # 41 function calls in 0.000 seconds
cProfile.run('sieve_without_eratostene(50)')  # 281 function calls in 0.000 seconds
cProfile.run('sieve_without_eratostene(100)')  # 643 function calls in 0.001 seconds
cProfile.run('sieve_without_eratostene(500)')  # 4073 function calls in 0.009 seconds

"""Вывод: однозначно, функция без использования алгоритма «Решето Эратосфена» показывает лучшие результаты"""
