s = 100
cnt = 0
n = int(input())
c = n
if 0 <= n and n <= 99:
    while n != s:
        s = (c//10) + (c%10)
        s = int(str((c%10)) + str(s)[-1])
        c = s
        cnt += 1
print(cnt)