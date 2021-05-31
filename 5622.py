A = input()
num = []
for i in A:
    if i in ['A','B','C']: num.append(2)
    elif i in ['D', 'E', 'F']: num.append(3)
    elif i in ['G', 'H', 'I']: num.append(4)
    elif i in ['J', 'K' , 'L']: num.append(5)
    elif i in ['M', 'N', 'O']: num.append(6)
    elif i in ['P', 'Q', 'R', 'S']: num.append(7)
    elif i in ['T', 'U', 'V']: num.append(8)
    elif i in ['W', 'X', 'Y', 'Z']: num.append(9)
res = 0
for i in num:
    res += i
res += len(num)
print(res)