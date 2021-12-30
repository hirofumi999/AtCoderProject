N, X = map(int, input().split())
DP = [''] * (N + 1)
DP[0] = 'P'
for i in range(1, N+1):
    DP[i] = 'B' + DP[i-1] + 'P' + DP[i-1] + 'B'
    print(DP[i])