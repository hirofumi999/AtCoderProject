from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = defaultdict(int)

for a in A:
    B[a] += 1

ans = N * (N - 1) * (N - 2) // 6

for key, value in B.items():

    if value >= 3:
        ans -= value * (value - 1) * (value - 2) // 6
    if value >= 2:
        ans -= (value * (value - 1) // 2) * (N - value)
print(ans)

