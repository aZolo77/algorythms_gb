"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random
import statistics

m = random.randint(1, 10)
size = 2 * m + 1
print(size)

arr = [i for i in range(size)]
random.shuffle(arr)

print(f'Список до сортировки:\n{arr}')


# Пирамидальная сортировка ("сортировка кучей"): O(n log n)
def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]

        heapify(nums, heap_size, largest)


def find_median(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


middle = len(arr) // 2
find_median(arr)
print(f'Список после сортировки:\n{arr}')
print(f'Медианой списка является:\n{arr[middle]}')

# Проверка
random.shuffle(arr)
print(statistics.median(arr))
