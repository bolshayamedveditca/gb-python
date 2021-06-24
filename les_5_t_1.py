number = int(input("введите количество предприятий"))
factory = {}
for i in range (0, number):
    hold = input('введите название предприятия и прибыль за каждый из четырех кварталов через пробел')
    hold = hold.split()
    factory[hold[0]] = [float(j) for j in hold[1:]]
    factory[hold[0]].append(sum(factory[hold[0]])/4)

middle = sum([elem[4] for elem in factory.values()])/number

print('прибыль этих предприятий ниже средней')
for key,value in factory.items():
    if value[4] < middle:
        print(key)

print('прибыль этих предприятий выше средней')
for key, value in factory.items():
    if value[4] > middle:
        print(key)

print('прибыль этих предприятий средняя')
for key,value in factory.items():
    if value[4] == middle:
        print(key)