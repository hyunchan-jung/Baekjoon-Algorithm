M, N = map(int,input().split())

a = [False, False] + [True]*(N-1)
p = []
for i in range(2, N+1):
    if a[i]:
        p.append(i)
        for j in range(i*2,N+1,i):
            a[j] = False

for i in range(M, N+1):
    if i in p:
        min_ = p.index(i)
        break
for i in range(N, M-1, -1):
    if i in p:
        max_ = p.index(i)
        break
[print(i) for i in p[min_:max_+1]]