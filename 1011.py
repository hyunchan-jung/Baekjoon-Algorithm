T = int(input())
res = []
for i in range(T):
    x, y = map(int, input().split())
    n = y - x
    M = 0
    m = 1
    cnt = 0
    while M < n:
        M += m
        cnt += 1
        if cnt % 2 == 0:
            m += 1
    res.append(cnt)
[print(i) for i in res]