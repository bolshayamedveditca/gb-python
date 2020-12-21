my_file = open('my_file.txt', 'w+')
print(f'Введите строку, по окончании ввода строки, нажмите enter,\n')
print(f'по окончании ввода текста нажмите enter 2 раза\n')
while True:
    x = input()
    if x == '':
        break
    else:
        my_file.write(f'{x} \n')

my_file.seek(0)

for el in my_file.readlines():
    y = el
    print(y)

my_file.close()