T = int(input())
a = []
b = []
plus = []
for i in range(T):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)
    plus.append(A+B)
for i in range(T):
    print('Case #{0}: {1} + {2} = {3}'.format(i+1, a[i], b[i], plus[i]))