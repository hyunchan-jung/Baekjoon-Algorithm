M = int(input()); N = int(input())
a = [False, False] + [True]*(N-1)
p = []
for i in range(2, N+1):
    if a[i]:
        p.append(i)
        for j in range(i*2,N+1,i):
            a[j] = False
try:
    min_sosu = M + a[M:].index(True)
    n = 0
    N = []
    for i in range(len(a)):
        if a[i]:
            N.append(n)
        n += 1
    sum_sosu = sum(N[N.index(min_sosu):])
    print(sum_sosu)
    print(min_sosu)
except ValueError: print(-1)