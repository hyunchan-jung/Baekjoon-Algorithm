import sys
L = []
while 1:
    n = int(sys.stdin.readline().strip())
    if n == 0: break
    L.append(n)

a = [False, False] + [True]*246911
p = []
for i in range(2, 246913):
    if a[i]:
        p.append(i)
        for j in range(i*2,246913,i):
            a[j] = False

res = []
for i in L:
    res.append(a[i+1:(i*2)+1].count(True))
[print(i) for i in res]