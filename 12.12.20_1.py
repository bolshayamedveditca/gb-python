from sys import argv

#(выработка в часах * ставка в час) + премия.
if len(argv) == 4:
    salary = (int(argv[1]) * int(argv[2])) + int(argv[3])
    print(f'Yours salary is {salary}')
else:
    print(f"count of arguments doesn't match. please input 'hours', 'cost' and 'premium'')

