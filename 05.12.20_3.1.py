import math

month = int(input('введите номер месяца\n'))

season = ['зима', 'весна', 'лето', 'осень']

i = math.floor(month/3) % 4

print(f'{month} месяц - это {season[i]}')