import timeit
array = input('введите числа через пробел ')

def time (arr, p):
    arr = [float(i) for i in arr.split()]

    n = max(filter(lambda x: x < 0, arr))
    n1 = arr.index(n)

    if p:
        print(n, n1)

time(array, True)
print(timeit.timeit(lambda: time(array, False), number = 100))
