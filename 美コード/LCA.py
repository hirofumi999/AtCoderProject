N = int(input())
X = [[] for i in range(N)]
for i in range(N - 1):
    x, y = map(int, input().split())
    X[x - 1].append(y - 1)
    X[y - 1].append(x - 1)

P = [-1] * N
DE = [0] * N
Q = [0]
while Q:
    i = Q.pop()
    for a in X[i][::-1]:
        if a != P[i]:
            P[a] = i
            DE[a] = DE[i] + 1
            X[a].remove(i)
            Q.append(a)

KK = 17
D = [[P[i] for i in range(N)]] + [[-1] * N for _ in range(KK - 1)]
for k in range(1, KK):
    for i in range(N):
        a = D[k - 1][i]
        if a > 0:
            D[k][i] = D[k - 1][a]


def lca(u, v):
    if DE[u] < DE[v]:
        u, v = v, u

    while DE[u] > DE[v]:
        d = DE[u] - DE[v]
        dd = d.bit_length() - 1
        u = D[dd][u]
    if u == v:
        return u

    for i in range(KK)[::-1]:
        if D[i][u] != D[i][v]:
            u = D[i][u]
            v = D[i][v]

    return D[0][u]


for _ in range(int(input())):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    c = lca(a, b)
    print(DE[a] + DE[b] - DE[c] * 2 + 1)
