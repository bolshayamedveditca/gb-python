number = int(input("пожалуйста,введите целое число число\n"))
max = 0
while number > 0:
    box = number%10
    number = number//10
    if max < box:
        max = box

print(f'наибольшая цифра в числе - {max}')

