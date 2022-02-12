N = int(input())
S = [ord(a) - ord('A') for a in input()]
mod = 998244353

DP = [[[0] * 10 for _ in range(1 << 10)] for __ in range(N + 1)]  # i番目まで見たときにで終わったコンテストのbit jと最後のコンテストk

for i, contest in enumerate(S, 1):
    DP[i][(1 << contest)][contest] = 1  # 初めてcontestに出る
    for j in range(1 << 10):
        for k in range(10):
            DP[i][j][k] += DP[i-1][j][k]  # i番目のコンテストに出ない
            DP[i][j][k] %= mod
            if contest == k:
                DP[i][j][k] += DP[i-1][j][k]  # i番目のコンテストに出る。最後のコンテストとi番目のコンテストが同じ
                DP[i][j][k] %= mod
            elif (j >> contest) & 1 != 1:  # i番目のコンテストに出る。最後のコンテストとi番目のコンテストが別
                DP[i][j | (1 << contest)][contest] += DP[i - 1][j][k]
                DP[i][j | (1 << contest)][contest] %= mod

ans = 0
for dp in DP[-1]:
    ans += sum(dp)
    ans %= mod
print(ans)
