N = []
S = set()
[N.append(int(input())) for i in range(10)]
[S.add(i%42) for i in N]
print(len(S))