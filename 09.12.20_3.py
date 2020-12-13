def my_funk(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print(f'вы ввели вовсе не числа, не могу их суммировать. попробуйте еще раз')
        return
    box = b + c
    print(f'{box}')
lst = []
a = 'x'
while a != 'q':
    lst = input(f'введите три числа через пробел\n').split(' ')
    lst = sorted(lst)
    if len(lst) != 3:
        print('вы ввели больше или меньше чисел, чем надо, либо иных символов. попробуйте еще раз')
        continue
    my_funk(*lst)
    a = input(f'введите "q" для завершения  или нажмите enter для продолжения')

