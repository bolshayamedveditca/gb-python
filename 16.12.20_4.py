namber = open('namber.txt', 'r+')
try:
    lst = namber.readlines()
    namber.seek(0)
    dic = {'one':'один','two':'два','three':'три','four':'четыре','five':'пять'}
    for line in lst:
        for k, v in dic.items():
            line = line.replace(k, v)
        namber.write(line)
finally:
    namber.close()
