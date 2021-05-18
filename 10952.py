A = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    A.append(a+b)
for i in A:
    print(i)