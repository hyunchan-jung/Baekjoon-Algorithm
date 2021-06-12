n = 0
nn = 0
N = []
while nn < 2147483648:
    n += 1
    nn += n
    N.append(nn)

def closer(a1, a2, b):
    if a1 is None: return a2
    if a2 is None: return a1
    return a1 if abs(a1 - b) < abs(a2 - b) else a2
def sweeping(A, B):
    clip = lambda idx: max(min(len(A) - 1, idx), 0)
    idx_a = 0
    while idx_a + 1 < len(A) and A[idx_a + 1] < B:
        idx_a += 1
    C = closer(A[clip(idx_a)], A[clip(idx_a + 1)], B)
    n = N.index(C)
    if C > B:
        return n-1
    else: return n

x = 1
y = 6
y = (y - x) // 2
cnt = sweeping(N, y)
if y >= 2 or y == 0:
    print((cnt+1)*2+1)
else: print(2)