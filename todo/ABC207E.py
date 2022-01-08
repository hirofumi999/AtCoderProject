N = int(input())
A = [[0] * (N + 1) for _ in range(N + 1)]
S = [[0] * i for i in range(N + 1)]
mod = 10 ** 9 + 7

for i, s in enumerate(input().split(), 1):
    l = len(s)
    if l >= 2:
        for j in range(1, N + 1):
            A[j][i] = ((int(s[:l // 2]) % j) * pow(10, l - l // 2, j) + int(s[l // 2:]) % j) % j
            if i >= 1:
                A[j][i] += A[j][i - 1]
                A[j][i] %= j
    else:
        for j in range(1, N + 1):
            A[j][i] = int(s) % j
            if i >= 1:
                A[j][i] += A[j][i - 1]
                A[j][i] %= j

DP = [[0] * (N + 1) for _ in range(N + 1)]  # i番目の数字まで見たときに、groupがj個できている時の個数
DP[0][0] = 1
S[0][0] = 1
for i in range(N + 1):
    for j in range(i + 1):
        for k in range(i + 1, N + 1):
            if A[j + 1][i] == A[j + 1][k]:
                DP[k][j + 1] += DP[i][j]
                DP[k][j + 1] %= mod
print(sum(DP[-1]) % mod)
