#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

arr = []
arr1 = []

for i in range(0, 15):
    arr.append(round(random.random()*50, 3))
    arr1.append(arr[i])

def merge(arr2):
    if len(arr2) > 1:
        half = len(arr2)//2
        left = arr2[:half]
        right = arr2[half:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        l = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr2[l] = left[i]
                i += 1
            else:
                arr2[l] = right[j]
                j += 1
            l += 1

        while i < len(left):
            arr2[l] = left[i]
            i += 1
            l += 1

        while j < len(right):
            arr2[l] = right[j]
            j += 1
            l += 1

merge(arr)
print(arr1)
print(arr)