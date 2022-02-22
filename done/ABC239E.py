from collections import deque

N, Q = map(int, input().split())
X = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
Query = [tuple(map(int, input().split())) for _ in range(Q)]

Q = deque()
Q.append(0)
Order = []
Num = [[]for _ in range(N)]

while Q:
    now = Q.popleft()
    Order.append(now)
    for nex in Edge[now]:
        Edge[nex].remove(now)
        Q.append(nex)

for now in Order[::-1]:
    num = [X[now]]
    for nex in Edge[now]:
        num.extend(Num[nex])
    num.sort()
    if len(num) > 20:
        num = num[-20:]
    Num[now] = num

for v, k in Query:
    print(Num[v - 1][-k])
