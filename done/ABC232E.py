H, W, K = map(int, input().split())
x_start, y_start, x_end, y_end = map(int, input().split())
mod = 998244353
DP = [0] * 4  # 4状態の推移　どちらでもない、xはok、yはok、xもyもok

if (x_start == x_end) and (y_start == y_end):
    DP[3] = 1
elif x_start == x_end:
    DP[1] = 1
elif y_start == y_end:
    DP[2] = 1
else:
    DP[0] = 1

for _ in range(K):
    dp = [0] * 4
    dp[3] = DP[2] + DP[1]
    dp[3] %= mod
    dp[2] = (DP[3] * (H - 1)) % mod + (DP[2] * (H - 2)) % mod + DP[0]
    dp[1] = (DP[3] * (W - 1)) % mod + (DP[1] * (W - 2)) % mod + DP[0]
    dp[2] %= mod
    dp[1] %= mod
    dp[0] = (DP[0] * ((H - 2) + (W - 2))) % mod + (DP[1] * (H - 1)) % mod + (DP[2] * (W - 1)) % mod
    dp[0] %= mod
    DP = dp
print(DP[3] % mod)
