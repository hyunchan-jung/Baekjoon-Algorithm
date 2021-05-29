T = int(input())
alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'
A = []
val = ''
for i in range(T):
    R, S = input().split()
    for j in S:
        val += j * int(R)
    A.append(val)
    val = ''
[print(i) for i in A]