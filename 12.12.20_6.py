#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import count, cycle
y = 3
x = 25
for i in count(y):
    print(i)
    if i == x:
        break
z = 1

lst = ['2',  'er', '23', 'sss', '2', 4, 6]
for i in cycle(lst):
    print(i)
    if z == 250:
        break
    z += 1




