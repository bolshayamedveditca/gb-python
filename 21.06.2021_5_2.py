import timeit
array = input('введите  числа через пробел ')
def time (arr, p):
    arr = [float(i) for i in arr.split()]

    x = 0
    for i in range(0, len(arr)):
        if arr[i] < 0:
            if x != 0:
                if arr[i] > x:
                    x = arr[i]
                    x1 = i
            else:
                x = arr[i]
                x1 = i
    if p:
        print(x, x1)

time(array, True)
print(timeit.timeit(lambda: time(array, False), number = 10000))

