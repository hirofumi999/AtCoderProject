from collections import deque

N, M = map(int, input().split())
X = [[]for _ in range(N)]
for _ in range(M):
    s_, t_, d_, ti_ = map(int, input().split())
    s_ -= 1
    t_ -= 1
    X[s_].append((t_, d_, ti_))
    X[t_].append((s_, d_, ti_))

DP = [[float('inf')] * N for _ in range(1 << N)]
DP[1][0] = 0
Q = deque()
Q.append((0,0))

while Q:
    now, S = Q.popleft()
    for nx, dist, limit in X[now]:
        if now + dist > limit:
            continue
        if (1 << nx) & S:
            continue
        S |= 1 << nx
        if DP[S][nx] > now + dist:
            DP[S][nx] = now + dist
            Q.append((nx, S))

print(DP)