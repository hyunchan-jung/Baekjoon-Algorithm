N, X = map(int,input().split())
A = [int(i) for i in input().split()]
AA = []
[AA.append(i) for i in A if i < X]
[print(i,end=' ') for i in AA]