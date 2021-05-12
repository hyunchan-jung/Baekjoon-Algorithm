# -*- coding: cp949 -*-
A = int(input())
listA = []
listB = []
mean = 0
count = 0
over_mean = 0

for i in range(A): # 테스트 케이스의 개수 A=5
    B = input().split()
    count = int(B[0])   # count = 학생의수  5
    for i in range(count):    # 학생의수 5
        mean += int(B[i+1])
    mean = mean/count
    for i in range(count):
        if int(B[i+1]) > mean:
            over_mean += 1
    listB.append(over_mean/count*100)
    mean = 0
    over_mean = 0
for i in range(len(listB)):
    print('{0:0.3f}%'.format(listB[i]))