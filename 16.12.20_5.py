namber_1 = open('namber_1.txt','w+')
try:
    x = []
    c = 0
    try:
        while True:
            x = input('введите числа с клавиатуры через пробел\n')
            namber_1.write(x + '\n')
            x = x.split(' ')
            for i in range(0, len(x)):
                c += int(x[i])
            print(c)
    except ValueError:
        print(c)

finally:
    namber_1.close()