import math

month = int(input('введите номер месяца\n'))

season = {0:'зима', 1:'весна', 2:'лето', 3:'осень'}

i = math.floor(month/3) % 4

print(f'{month} месяц - это {season[i]}')