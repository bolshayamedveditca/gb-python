from functools import reduce
lst = list(range(100, 1001, 2))
print(f' {lst}\n{reduce(lambda x,y: x * y, lst)}')