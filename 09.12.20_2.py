
def data(**kvargs):
    data_1 = str()
    for k, v in kvargs.items():
        data_1 += k + ' - ' + v + ', '
    print(f'{data_1}')


lst = {'имя' : 'имя', 'фамилия' : 'фамилию', 'год' : 'год', 'город' : 'город', 'e-mail' : 'e-mail', 'телефон' : 'телефон'}
for k, v in lst.items():
    lst[k] = input(f'Введите {v}\n')

data(**lst)

