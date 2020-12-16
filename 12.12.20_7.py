def fact(n):
    x = 1
    i = 1
    for i in range(1, n):
        x = x * i
        yield x

for el in fact(10):
    print(el)

