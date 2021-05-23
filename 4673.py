def d(n):
    sum = 0
    N = str(n)
    for i in N:
        sum += int(i)
    sum += n
    return sum

a = set()
b = []
 
for i in range(1,10001):
    b.append(i)
    a.add(d(i))
    
c = [x for x in b if x not in a]

for i in c:
    print(i)