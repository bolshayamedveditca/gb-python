# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

import sys

str1 = input('Введите целые числа через пробел')
summa = []
str2 = str1.split()
str2 = [int(i) for i in str2]
for i in str2:
    s = 0
    while i > 0:
        s += i % 10
        i = i // 10
    summa.append(s)

print('наименьшая сумма цифр в числе')
print(min(summa))
print('наибольшая сумма цифр в числе')
print(max(summa))

print(sys.getrefcount(str1))    # 2 - не меняется в зависимости от вводимых данных
print(sys.getrefcount(str2[0])) # 4 - не меняется в зависимости от вводимых данных
print(sys.getrefcount(summa[0]))# 24 - не меняется в зависимости от вводимых данных
print(sys.getrefcount(i))       # 182 - меняется не существенно в зависимости от вводимых данных
print(sys.getrefcount(s))       # 19 - меняется в пределах 100

print(sys.getsizeof(str1) + sys.getsizeof(str2) + sys.getsizeof(summa) + sys.getsizeof(i) + sys.getsizeof(s))
# 894 byte (на одном наборе данных для всех вариантов) - также самый неэффективный вариант
# по количеству ссылок это самый не эффективный вариант

#pithon 3.7.9 windows 10 64