import heapq
from bisect import bisect_left

N, M, R, T = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append([b, c])
    Edge[b].append([a, c])
ans = 0
for goal in range(N):
    dist_list = []
    A = [goal]
    Dist = [float('inf')] * N
    Dist[goal] = 0
    Done = [False] * N
    while A:
        d, now = divmod(heapq.heappop(A), 10 ** 4)
        if Done[now]:
            continue
        dist_list.append(d * R)
        Done[now] = True
        for nex, take in Edge[now]:
            if Dist[nex] > Dist[now] + take:
                Dist[nex] = Dist[now] + take
                heapq.heappush(A, (Dist[nex] * 10 ** 4 + nex))
    for i, d in enumerate(dist_list[1:]):
        idx = bisect_left(dist_list[1:], d * T // R)
        if i <= idx:
            idx -= 1
        ans += idx

print(ans)