from bisect import bisect_left
from itertools import accumulate


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ACC = [0] + list(accumulate(A))

if K >= ACC[-1]:
    ans = 0
    for a in A:
        ans += (1 + a) * a // 2
    print(ans)
    exit()


def calc(n):
    idx = bisect_left(A, n)
    if idx >= N:
        return False
    return (ACC[-1] - ACC[idx]) - n * (N - idx) >= K


start = -5
end = 10 ** 10

while start + 1 < end:
    mid = (start + end) // 2
    if calc(mid):
        start = mid
    else:
        end = mid

ans = 0

for a in A[::-1]:
    if a > end:
        ans += (a + end + 1) * (a - end) // 2
        K -= a - end
    else:
        break
ans += end * K

print(ans)
