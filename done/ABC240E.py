import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.buffer.readline

N = int(input())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Edge[u].append(v)
    Edge[v].append(u)

Ans = [0] * N
Done = [0] * N
Done[0] = 1
cnt = 1


def dfs(start=0):
    global cnt, Ans
    Done[start] = True
    flag = True
    mi = float('inf')
    ma = -1
    for nex in Edge[start]:
        if Done[nex]:
            continue
        flag = False
        tmp = dfs(nex)
        mi = min(mi, tmp[0])
        ma = max(ma, tmp[1])
    if flag:
        Ans[start] = (cnt, cnt)
        cnt += 1
    else:
        Ans[start] = (mi, ma)
    return Ans[start]


dfs(0)
for ans in Ans:
    print(*ans)