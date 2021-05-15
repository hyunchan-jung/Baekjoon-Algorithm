N = int(input())
M = input().split()
Max = max(M)
K = []
A = 0
for i in range(len(M)):
    M[i] = int(M[i])
    M[i] = M[i]/int(Max)*100
    K.append(M[i])
    A += M[i]
print(A/len(M))