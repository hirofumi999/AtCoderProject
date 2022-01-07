import sys

input = sys.stdin.buffer.readline

N, M = map(int, input().split())
Map = [[float('inf')] * N for _ in range(N)]
ans_now = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Map[a][b] = c
    ans_now += c

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if Map[i][j] > Map[i][k] + Map[k][j]:
                if Map[i][j] == float('inf'):
                    Map[i][j] = Map[i][k] + Map[k][j]
                    ans_now += Map[i][j]
                else:
                    ans_now += Map[i][k] + Map[k][j] - Map[i][j]
                    Map[i][j] = Map[i][k] + Map[k][j]
    ans += ans_now

print(ans)
