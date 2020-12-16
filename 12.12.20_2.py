lst = input('Введите числа в через пробел')
lst_2 = lst.split(' ')
lst_2 = list(map(int, lst_2))
def my_gen(lst):
    i = 1
    while i < len(lst):
        if lst[i-1] < lst[i]:
            yield lst[i]
        i += 1
lst_1 = list(my_gen(lst_2))
print(lst_1)