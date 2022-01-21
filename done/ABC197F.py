from collections import deque

N, M = map(int, input().split())
Edge = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    a -= 1
    b -= 1
    Edge[a].append((b, c))
    Edge[b].append((a, c))

Q = deque()
Q.append((0, N - 1, 0))
done = {(0, N - 1)}
ans = float('inf')
while Q:
    now1, now2, dist = Q.popleft()
    if 2 * dist > ans:
        break
    if now1 == now2:
        ans = min(ans, dist * 2)
    for nex1, a1 in Edge[now1]:
        for nex2, a2 in Edge[now2]:
            if nex2 == now1:
                ans = min(ans, dist * 2 + 1)
            if a1 == a2 and (nex1, nex2) not in done:
                Q.append((nex1, nex2, dist + 1))
                done.add((nex1, nex2))

print(ans if ans != float('inf') else -1)