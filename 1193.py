# -*- coding: cp949 -*-
N = int(input())
A = 0
B = 0
while B < N:
    A += 1
    B += A
if A % 2 == 0: # 짝수
    bm = 1 + (B-N)
    bj = A - (B-N)
else : # 홀수
    bm = A - (B-N)
    bj = 1 + (B-N) 
print('{0}/{1}'.format(bj, bm))