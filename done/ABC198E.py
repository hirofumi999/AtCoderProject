from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)


def dfs(now):
    global Done, Ans, Edge, Colors
    for nex in Edge[now]:
        if Done[nex]:
            continue
        Done[nex] = True
        if Colors[Color[nex]] == 0:
            Ans.add(nex + 1)
        Colors[Color[nex]] += 1
        dfs(nex)
        Colors[Color[nex]] -= 1


N = int(input())
Color = list(map(int, input().split()))
Colors = defaultdict(int)
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

Done = [False] * N
Done[0] = True
Ans = {1}
Colors[Color[0]] += 1
dfs(0)
for i in range(N + 1):
    if i in Ans:
        print(i)


