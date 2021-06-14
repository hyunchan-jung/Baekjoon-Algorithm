a = [False, False] + [True]*999
p = []
for i in range(2, 1001):
    if a[i]:
        p.append(i)
        for j in range(i*2,1001,i):
            a[j] = False

T = int(input())
N = map(int,input().split())
cnt = 0
for i in N:
    if i in p:
        cnt += 1
print(cnt)