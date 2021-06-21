array = input('введите  числа через пробел ')
array = [float(i) for i in array.split()]

n = max(filter(lambda x: x < 0, array))
n1 = array.index(n)

print(n, n1)
