words = input('введите слова через пробел\n')
word = str()
for i in words:
    if len(word)< 10 and i != ' ':
        word += i
    else:
        print(f'{word}')
        word = i if i != ' ' else ''
print(f'{word}')


