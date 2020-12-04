income = float(input("пожалуйста,введите сумму выручки\n"))
costs = float(input("пожалуйста,введите сумму издержек\n"))

if income > costs:
    print('Фирма рентабельна')
    profit = (income - costs) / (income/100)
    print(f'Рентабельность составляет {profit:.2f}%')
    workers = int(input("пожалуйста,введите количество сотрудников в фирме\n"))
    earnings = (income - costs) / workers
    print(f'прибыль для каждого сотрудника составляет {earnings:.2f}')
elif income < costs:
    print('Фирма нерентабельна')
else:
    print('Фирма работает в 0')

