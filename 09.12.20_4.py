def my_funk(x, y):
    x = int(x)
    y = int(y)
    result = 1
    for i in range(0, abs(y)):
        result = result * 1/x
    print(f'{result}')

    result_1 = x ** y     #второй вариант. не стала выносить в отдельный файл
    print(f'{result_1}')

print('введите целое положительное и целое отрицательное числа')
lst = input('через пробел\n').split()
my_funk(*lst)