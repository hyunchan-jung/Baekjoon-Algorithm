A = input()
A = A.upper()
B = []
a = []

for i in A:
    if i not in B:
        B.append(i)
        
for i in B:
    a.append(A.count(i))
    
if a.count(max(a)) > 1:
    print('?')
else:
    print(B[a.index(max(a))])