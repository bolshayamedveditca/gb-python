long = int(input('Введите длину списка\n'))

lst = []
while long > 0:
    lst.append(input('введите элемент списка\n'))
    long -= 1

for el in lst:
    box = el
    try:
        box = int(el)
    except ValueError:
        try:
            box = float(el)
        except ValueError:
            try:
                box = bool(el)
            except ValueError:
                pass
    print(f'{el} - {type(box)}')




