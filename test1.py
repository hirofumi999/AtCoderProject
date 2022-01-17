S = input()
N = len(S)
M = int(input())
C = list(map(int, input().split()))
mod =  998244353
c = (1 << 10) - 1
for c_ in C:
    c ^= 1 << c_

DP = [[0] * (1 << M) for _ in range(2)]

for s in S:
    x = int(s)
    dp = [[0] * (1 << M) for _ in range(2)]
    dp[0][x] = sum(DP[0]) * 10 + x
    for i in range(1 << M):
        for j in range(10):
            if j in C:
                cidx = C.index(j)
                if (i >> cidx) & 1 == 1:
                    dp[1][i] = DP[1][i] * 10 + j
                else:
                    dp[1][i^(1 << j)] = DP[1][i] * 10 + j
            else:
                dp[1][i] = DP[1][i] * 10 + j
    DP = dp
print(sum(DP))