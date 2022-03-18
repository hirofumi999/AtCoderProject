T = int(input())
mod = 998244353
for _ in range(T):
    N = int(input())
    S = input()
    S1 = S[:(N + 1) // 2]
    S2 = S[N // 2:]
    DP = [0] * 2 # 0 未確定 1 確定済
    DP[0] = 1
    flag = True
    for s1 in S1:
        ch = ord(s1) - ord('A')
        dp = [0] * 2
        dp[0] = DP[0]
        dp[1] = (DP[0] * ch + DP[1] * 26) % mod
        DP = dp
    for s1, s2 in zip(S1[::-1], S2):
        if s1 > s2:
            flag = False
            break
        elif s1 == s2:
            continue
        else:
            break
    ans = DP[1]
    if flag:
        ans += DP[0]
    print(ans % mod)