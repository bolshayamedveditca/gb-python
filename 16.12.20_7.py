import json
with open('firm.txt', 'r+') as firm:

    profit = {}
    average_profit = {}
    c = 0
    arr = []
    lst = firm.readlines()
    for i in range(0, len(lst)):
        arr.append(lst[i].split(' '))
        x = (int(arr[i][2]) - int(arr[i][3]))
        profit[arr[i][0]] = x
        if x > 0:
            c += x
    average_profit = {'average_profit': (c/len(lst))}
    #print([profit,average_profit])
    with open("firm.json", "w") as write_file:
        json.dump([profit,average_profit], write_file)







