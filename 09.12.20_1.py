def dev(a, b):
    a = float(a)
    b = float(b)
    devision = a / b
    return devision


def rnd(devision):
    x = 2
    devision = str(devision)
    if devision.find('e-') >= 0:
        return None
    devision = devision.split('.')
    for el in devision[1]:
        if el == '0':
            x += 1
        else:
            break
    return x

def ask():
    q = input('введите q, если хотите выйти \n')
    if q == 'q':
        return False
    return True

while True:
    devidend = input('введите делимое \n')
    devider = input('введите делитель \n')
    if devidend == 'q':
        break
    try:
        devision = dev(devidend, devider)
    except (ValueError, ZeroDivisionError):
        print('Данные введены некорректно, попробуйте снова')
        continue
    if rnd(devision) != None:
        print(f'{devidend}/{devider} = {devision:.{rnd(devision)}f}')
    else:
        print(f'{devidend}/{devider} = {devision}')

    if not ask():
        break