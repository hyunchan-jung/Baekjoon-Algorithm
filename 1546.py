N = int(input())
M = input().split()
MM = []
[MM.append(int(i)) for i in M]
Max = max(MM)
A = 0
for i in range(len(M)):
    M[i] = int(M[i])
    M[i] = M[i]/int(Max)*100
    A += M[i]
print(A/len(M))