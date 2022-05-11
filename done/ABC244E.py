N, M, K, S, T, X = map(int, input().split())
S -= 1
T -= 1
X -= 1
Edge = [[] for _ in range(N)]
mod = 998244353
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)


DP = [[[0] * 2 for _ in range(N)] for __ in range(K + 1)]  # これまでに通った辺の数、いる頂点、Xを通った回数

DP[0][S][S == X] = 1

for edge_cnt in range(K):
    for point in range(N):
        if point == X:
            for boo in range(2):
                for prev in Edge[point]:
                    DP[edge_cnt + 1][point][(boo + 1) % 2] += DP[edge_cnt][prev][boo]
                    DP[edge_cnt + 1][point][(boo + 1) % 2] %= mod
        else:
            for boo in range(2):
                for prev in Edge[point]:
                    DP[edge_cnt + 1][point][boo] += DP[edge_cnt][prev][boo]
                    DP[edge_cnt + 1][point][boo] %= mod

print(DP[K][T][0] % mod)

