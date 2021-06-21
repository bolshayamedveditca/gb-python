array = input('введите  числа через пробел ')
array = [float(i) for i in array.split()]
array2 = []
x1 = 0

for i in range(0, len(array)):
    if array[i] < 0:
        array2.append(array[i])

x = array2[0]

for i in range(1, len(array2)):
    if array2[i] > x:
        x = array2[i]
for i in range(0, len(array)):
    if x == array[i]:
        x1 = i

print(x, x1)


