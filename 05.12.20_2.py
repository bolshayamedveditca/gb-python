lst = []
while True:
    el = input('введите элемент списка или "q" для завершения ввода\n')
    if el == "q":
        break
    lst.append(el)
print(lst)
for i in range(0 , len(lst)-1 , 2):
    lst[i],lst[i+1] = lst[i+1],lst[i]
print(lst)
