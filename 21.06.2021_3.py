array = []

array = input('введите целые числа через пробел ')
array = [int(i) for i in array.split()]

ma = array[0]
mi = array[0]
n1 = 0
n2 = 0

for i in range(1, len(array)):
    if array[i] > ma:
        ma = array[i]
        n1 = i
    elif mi > array[i]:
        mi = array[i]
        n2 = i

array[n1] = mi
array[n2] = ma

print(array)
