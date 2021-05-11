import sys
A = input()
B = []
count = 0
score = 0

for i in sys.stdin:
    B.append(i.strip())

for i in range(len(B)):
    for j in range(len(B[i])):
        if B[i][j] == 'O':
            count += 1
            score += count
        elif B[i][j] == 'X':
            count = 0
    print(score)
    score = 0
    count = 0