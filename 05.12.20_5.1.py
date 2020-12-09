lst = [4, 8, 35, 42]
i = int(input('введите целое натуральное число\n'))
print(f'{lst}')

for el in range(0,len(lst)):
    if i < lst[el]:
        lst.insert(el,i)
        break
    elif i == lst[el]:
        lst.insert(el+1,i)
        break
print(f'{lst}')
