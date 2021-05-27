S = input()
res = []
alp = 'abcdefghijklmnopqrstuvwxyz'

for i in alp:
    try:
        res.append(S.index(i))
    except ValueError:
        res.append('-1')
[print(int(i),end=' ') for i in res]