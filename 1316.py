N = int(input())
for i in range(N):
    a = 1
    A = input()
    B = set()
    for j in range(len(A)):
        if A.count(A[j]) != 1:
            B.add(A[j])
    for k in B:
        C = A.index(k)
        cnt = A.count(k)
        for l in range(cnt):
            if A[C+l:].index(k) != 0:
                N -= 1
                a = 0
                break
        if a == 0: break
print(N)
# 다른방법으로도 풀기

N = int(input())
for i in range(N):
    A = input()
    for j in range(len(A)-1):
        if A[j] != A[j+1] and A[j] in A[j+1:]:
            N -= 1
            break
print(N)