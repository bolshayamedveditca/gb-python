lst = input('Введите числа в через пробел\n')
lst_2 = lst.split(' ')

def my_gen(lst):
    dic = {}
    for el in lst:
        if el == '':
            continue
        if el in dic:
            dic[el] += 1
        else:
            dic[el] = 1
    #print(dic)
    for k, v in dic.items():
        if v == 1:
            yield k

lst_1 = list(my_gen(lst_2))
print(lst_1)



