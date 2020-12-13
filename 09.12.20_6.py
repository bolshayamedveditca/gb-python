def int_funk(*args):
    string = ''
    for el in args:
        string += ' ' + str(el).capitalize()
    return string

words = input('введите слова через пробел\n').split(' ')
print(f'{int_funk(*words)}')
