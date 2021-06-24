term1 = input("введите первое слагаемое")
term2 = input('введите второе слагаемое')
l = len(term1) if len(term1) > len(term2) else len(term2)
c =len(term1)-len(term2)
if c > 0:
    for i in range(0,c):
        term2 = "0" + term2
elif c < 0:
    for i in range (0,c):
        term1 = "0" + term1

summa = [0 for i in range(0, l+1)]
table = '0123456789abcdef'
for i in range(l-1,-1,-1):
    print(i)
    val = table.index(term1[i]) + table.index(term2[i])
    print(val)
    if len(summa) <= i:
        summa.append(0)
    summa[i] += val
    if summa[i] > 15:
        summa[i-1] += 1
        summa[i] = summa[i]%16
        print(summa)
while summa[0] == 0:
    summa.pop(0)
print(''.join([table[i]for i in summa]))