N = int(input())
Cities = [tuple(map(int, input().split())) for _ in range(N)]


def dist(a, b):
    global Cities
    return abs(Cities[a][0] - Cities[b][0]) + abs(Cities[a][1] - Cities[b][1]) + max(0, Cities[b][2] - Cities[a][2])


ans = float('inf')
DP = [[float('inf')] * N for _ in range(1 << N)]
DP[1][0] = 0
for i in range(1 << N):
    for j in range(N):
        if (i >> j) & 1 == 1:
            continue
        for k in range(N):
            if (i >> k) & 1 == 1:
                DP[i | (1 << j)][j] = min(DP[i | (1 << j)][j], DP[i][k] + dist(k, j))
    if i == (1 << N) - 1:
        for j in range(N):
            ans = min(ans, DP[i][j] + dist(j, 0))
print(ans)
