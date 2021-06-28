# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

import sys
str1 = input('Введите целые числа через пробел')
summa = []
str2 = str1.split()

for i in str2:
    summa.append(sum([int(j) for j in i]))

print('наименьшая сумма цифр в числе')
print(min(summa))
print('наибольшая сумма цифр в числе')
print(max(summa))

print(sys.getrefcount(str1))    # - 2 не меняется в зависимости от вводимых данных
print(sys.getrefcount(str2[0])) # - 2 не меняется в зависимости от вводимых данных
print(sys.getrefcount(summa[0])) #- 11 меняется не существенно в зависимости от вводимых данных
print(sys.getrefcount(i))       # - 3 не меняется в зависимости от вводимых данных

print(sys.getsizeof(str1) + sys.getsizeof(str2) + sys.getsizeof(summa) + sys.getsizeof(i))
# 846 byte (на одном наборе данных для всех вариантов) один из двух лучших результатов
#по количеству ссылок - это самый эффективный вариант решения задачи

#pithon 3.7.9 windows 10 64