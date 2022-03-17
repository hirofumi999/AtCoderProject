N, M = map(int, input().split())
Edge = [tuple(map(int, input().split())) for _ in range(M)]
Used = [False] * M
Map = [[float('inf')] * N for _ in range(N)]

for a, b, c in Edge:
    a -= 1
    b -= 1
    Map[a][b] = c
    Map[b][a] = c

for i in range(N):
    for j in range(N):
        for k in range(N):
            Map[i][j] = min(Map[i][k] + Map[k][j], Map[i][j])
            Map[j][i] = Map[i][j]
ans = 0
for a, b, c in Edge:
    a -= 1
    b -= 1
    flag = True
    for k in range(N):
        if Map[a][k] + Map[k][b] <= c:
            flag = False
            break
    if not flag:
        ans += 1
print(ans)