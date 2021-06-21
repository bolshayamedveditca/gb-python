import timeit
array = input('введите  числа через пробел ')

def time (arr, p):
    arr = [float(i) for i in arr.split()]
    array2 = []
    x1 = 0

    for i in range(0, len(arr)):
        if arr[i] < 0:
            array2.append(arr[i])

    x = array2[0]

    for i in range(1, len(array2)):
        if array2[i] > x:
            x = array2[i]
    for i in range(0, len(arr)):
        if x == arr[i]:
            x1 = i
    if p:
        print(x, x1)

time(array, True)
print(timeit.timeit(lambda: time(array, False), number = 10000))

