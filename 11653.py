N = int(input())
res = []
while N != 1:
    n = 2
    while 1:
        if N % n == 0:
            res.append(n)
            N = N // n
            break
        else: n += 1
[print(i) for i in res]