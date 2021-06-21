array = []
array2 = {}

array = input('введите целые числа через пробел ')
array = [int(i) for i in array.split()]
x1 = 0
n2 = array[0]

for i in range(0, len(array)):
    x = 0
    for n in range(0, len(array)):
        if array[n] == array[i]:
            x += 1
            array2[array[i]] = x
    if x > x1:
        x1 = x
        n2 = array[i]

print(str(x1) + ' чисел ' + str(n2))
