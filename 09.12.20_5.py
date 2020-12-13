def result(x, res, *args):
    for el in args:
        if el != x:
            el = float(el)
            res += el
        else:
            return res
    return res

x = 'x'
res = 0
lst = []
while x not in lst:
    print(f'введите числа через пробел, для завершения введите "{x}",')
    lst = input('для продолжения - enter\n')
    lst = lst.split(' ')
    res = result(x, res, *lst)
    print(f'{res}')
