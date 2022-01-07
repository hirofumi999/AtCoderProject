N, M = map(int, input().split())
mod = 10 ** 9 + 7
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
Distance = [set() for _ in range(N)]
Distance[0].add(0)
Num = [0] * N
Num[0] = 1
Done = [False] * N
Done[0] = True
flag = False
for distance in range(N):
    if N - 1 in Distance[distance]:
        break
    for now in Distance[distance]:
        Done[now] = True
    for now in Distance[distance]:
        for nex in Edge[now]:
            if Done[nex]:
                continue
            Distance[distance + 1].add(nex)
            Num[nex] += Num[now]
            Num[nex] %= mod

print(Num[-1] % mod)
