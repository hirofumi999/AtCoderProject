from collections import deque

N = int(input())
Color = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
Done = [0] * N
Done[0] = 1
Q = deque()
Q.append((0, {Color[0]}))
Ans = [0] * N
Ans[0] = 1
while Q:
    now, color = Q.pop()
    color.add(Color[now])
    for nex in Edge[now]:
        if Done[nex]:
            continue
        if Color[nex] not in color:
            Ans[nex] = 1
        Done[nex] = 1
        Q.append((nex, color))
for i, ans in enumerate(Ans, 1):
    if ans:
        print(i)