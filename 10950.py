B = []
T = int(input())
for i in range(T):
    A = input().split()
    B.append(A)
for i in range(len(B)):
    print(int(B[i][0]) + int(B[i][1]))