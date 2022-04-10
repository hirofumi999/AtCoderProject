from collections import deque


N, M = map(int, input().split())
Edge = [tuple(map(int, input().split())) for _ in range(M)]

in_num = [0] * N
in_edge = [[] for _ in range(N)]
out_num = [0] * N


for i, (u, v) in enumerate(Edge):
    u -= 1
    v -= 1
    in_edge[v].append([u, 0])
    in_num[v] += 1
    out_num[u] += 1

Q = deque()

for idx, (i, o) in enumerate(zip(in_num, out_num)):
    if o == 0:
        Q.append(idx)

while Q:
    idx = Q.pop()
    for i, edge in enumerate(in_edge[idx]):
        in_edge[idx][i][1] = 1
        out_num[edge[0]] -= 1
        if out_num[edge[0]] == 0:
            Q.append(edge[0])


ans = set()
for i in range(N):
    for edge in in_edge[i]:
        if edge[1] == 0:
            ans.add(i)
            ans.add(edge[0])

print(len(ans))
