N = int(input())
A1 = list(map(int, input().split()))

DP1 = [float('inf')] * (N + 2)
DP1[0] = 0

DP2 = [float('inf')] * (N + 2)
DP2[0] = 0
A2 = A1[1:].copy() + [A1[0]]

for i, a in enumerate(A1, 2):
    DP1[i] = min(DP1[i - 1], DP1[i - 2]) + a

for i, a in enumerate(A2, 2):
    DP2[i] = min(DP2[i - 1], DP2[i - 2]) + a
print(min(DP1[-2], DP2[-2], DP1[-1], DP2[-1]))

