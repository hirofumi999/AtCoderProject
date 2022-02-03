import heapq

N, M = map(int, input().split())
Height = list(map(int, input().split()))
Edge = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if Height[u] > Height[v]:
        Edge[u].append([v, 0])
        Edge[v].append([u, (Height[u] - Height[v])])
    else:
        Edge[u].append([v, (Height[v] - Height[u])])
        Edge[v].append([u, 0])

Done = [float('inf')] * N
Done[0] = 0
Q = [0]

while Q:
    now_ = heapq.heappop(Q)
    fun, now = divmod(now_, 10**6)
    for nex, cost in Edge[now]:
        if Done[nex] > fun + cost:
            Done[nex] = fun + cost
            heapq.heappush(Q, (fun + cost) * 10 ** 6 + nex)
ans = 0
for i in range(1, N):
    ans = max(ans, Height[0] - Height[i] - Done[i])

print(ans)