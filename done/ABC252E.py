from collections import deque

N, M = map(int, input().split())

Edge = [[] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, c, i + 1))
    Edge[b].append((a, c, i + 1))


Roads = deque([0])
Done = [float('inf')] * N
Done[0] = 0
Done_road = [-1] * N


while Roads:
    now = Roads.popleft()
    for nex, c, i in Edge[now]:
        if Done[nex] > Done[now] + c:
            Done[nex] = Done[now] + c
            Done_road[nex] = i
            Roads.append(nex)


print(*Done_road[1:])