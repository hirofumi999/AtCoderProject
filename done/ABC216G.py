from collections import deque
N, M = map(int,input().split())

LRX = []
for i in range(M):
    l, r, x = map(int, input().split())
    l -= 1
    LRX.append((l, r, x, i))
LRX.sort(key=lambda x: x[1])

A = [0] * N
Q = deque()
FT = [0] * (N + 2)  # BITを使う


def BIT_query(idx):
    idx += 1
    res_sum = 0
    while idx > 0:
        res_sum += FT[idx]
        idx -= idx&(-idx)
    return res_sum


def BIT_update(idx,x):
    idx += 1
    while idx <= N:
        FT[idx] += x
        idx += idx&(-idx)
    return



q = 0
for l, r, x, i in LRX:
    while q < r:
        Q.append(q)
        q += 1
    n = x - (BIT_query(r) - BIT_query(l - 1))
    for j in range(n):
        p = Q.pop()
        A[p] = 1
        BIT_update(p, 1)

print(*A)