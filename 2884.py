H, M = map(int, input().split())
if H >=0 and H <= 23 and 0 <= M and M <= 59:
    M -= 45
    if M < 0:
        M += 60
        H -= 1
        if H < 0:
            H += 24
    print(H, M)