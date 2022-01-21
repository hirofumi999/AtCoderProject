N = int(input())
A = list(map(int, input().split()))
n = N - 1
ans = float('inf')
for i in range(1 << n):
    ret = 0
    now = A[0]
    for j in range(n):
        if (i >> j) & 1 == 1:
            ret ^= now
            now = A[j + 1]
        else:
            now |= A[j + 1]
    ret ^= now
    ans = min(ans, ret)
print(ans)
