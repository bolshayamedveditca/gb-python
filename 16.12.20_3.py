payment = open('payment.txt', 'r+')
lst = payment.readlines()
d = 0
name = []
words = []
for el in lst:
    for el2 in el.split():
        words.append(el2)
for i in range(1, len(words), 2):
    if int(words[i]) < 20000:
        print(words[i-1])
    d += int(words[i])
print(f'имеют зарплату ниже 20 000')
print(f'средняя зарплата на предприятии {(d/len(lst)):.3f}')