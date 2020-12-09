i = 0
keys_food = ("название","цена","вес","количество")
lst = list()
c = True
while c:
    dict_food = {}
    for k in keys_food:
        info = input(f"Введите параметр товара {k} для продолжения, или 'q' для выхода\n")
        if info == 'q':
            c = False
            break
        dict_food[k] = info
    if info != 'q':
        lst.append((i, dict_food))
    i += 1

for el in lst:
    print(el)