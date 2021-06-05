N = int(input())
n = 1
nn = 2
if N == 1: print(1)
else:
    while True:
        if N <= 1 + (n * 6):
            print(nn)
            break
        n += nn
        nn += 1