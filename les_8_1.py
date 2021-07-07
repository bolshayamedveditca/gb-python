#строка s длиной n

import hashlib
s = input('введите строку ')
dicti = {}

def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    if h_subs in dicti:
        return
    dicti[h_subs] = {'num' : 0, 'name' : t}
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            dicti[h_subs]['num'] += 1

for c in range(0, len(s)-1):
    spam = ''
    for i in range(c, len(s)-1):
        spam += s[i]
        rabin_karp(s, spam)

print('подстроки, которые встречаются в строке более одного раза')
for i in dicti.values():
    if i['num'] > 1:
        print(i)