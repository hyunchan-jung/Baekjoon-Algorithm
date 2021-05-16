T = int(input())
Case = []
for i in range(T):
    A, B = map(int, input().split())
    Case.append(A + B)
for i in range(T):
    print('Case #{0}: {1}'.format(i+1, Case[i]))