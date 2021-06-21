array = []
array2 = []

array = input('введите целые числа через пробел')
array = array.split()
for i in range(0, len(array)):
    if int(array[i]) % 2 == 0:
        array2.append(str(i))

print('номера ячеек, в которых хранятся четные числа')
print(array2)
