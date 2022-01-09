A = input()
N = len(A)
S = [0] * 26
for a in A:
    S[ord(a) - ord('a')] += 1
mod = 998244353

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]


def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return (fact[n] * factinv[r] % mod) * factinv[n - r] % mod


for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


DP = [0] * (N + 1)
DP[0] = 1
for i, value in enumerate(S, 1):
    dp = [0] * (N + 1)
    for j in range(N + 1):
        for k in range(min(value + 1, j + 1)):
            dp[j] += DP[j - k] * cmb(j, k)
            dp[j] %= mod
    DP = dp
print(sum(DP[1:]) % mod)