#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random

arr = []
arr1 = []

for i in range(0, 15):
    arr.append(random.randint(-100,100))
    arr1.append(arr[i])

def bubble(arr2):
    i = 0
    c = 0
    while True:
        if arr2[i+1] > arr2[i]:
            arr2[i],arr2[i+1] = arr2[i+1],arr2[i]
            c = 1
        i += 1
        if i == 14 and c == 1:
            i = 0
            c = 0
        elif i == 14 and c == 0:
            break
    return(arr2)

print(arr1)
print(bubble(arr))
