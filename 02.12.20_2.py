time_seconds = int(input("пожалуйста,введите время в секундах\n"))
hours = time_seconds//3600
minutes = (time_seconds%3600)//60
seconds = time_seconds%60

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

