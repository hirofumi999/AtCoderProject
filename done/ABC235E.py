class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            if not self.same_check(x, y):
                self.size[y] += self.size[x]
                self.size[x] = 0
            self.par[x] = y
        else:
            if not self.same_check(x, y):
                self.size[x] += self.size[y]
                self.size[y] = 0
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def siz(self, x):
        x = self.find(x)
        return self.size[x]


N, M, Q = map(int, input().split())
UF = UnionFind(N)
Edge = []
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    Edge.append((a, b, c, 0))
for i in range(Q):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    Edge.append((u, v, w, i + 1))

Edge.sort(key=lambda x: x[2])
Ans = [False] * Q
for e1, e2, weight, edge_num in Edge:
    if UF.same_check(e1, e2):
        continue
    if edge_num:
        Ans[edge_num - 1] = True
    else:
        UF.union(e1, e2)
for ans in Ans:
    if ans:
        print('Yes')
    else:
        print('No')