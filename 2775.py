T = int(input())
res = []
for i in range(T):
    k = int(input())
    n = int(input())
    L = list(range(1,n+1))
    
    for j in range(k):
        for m in range(1,n):
            L[m] += L[m-1]
    res.append(L[n-1])
[print(i) for i in res]