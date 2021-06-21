array = []

for i in range(2, 9):
    array[i] = 0
    for n in range(2, 99):
        if n % i == 0:
            array[i] += 1

for i in range(2, 9):
    print('в числовом ряду от 2 до 99 на {} делится нацело {} чисел'.format(i, array[i]))
