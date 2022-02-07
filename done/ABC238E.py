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


N, Q = map(int, input().split())
Edge = [[] for _ in range(N)]
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1  # 0-indexの半開区間に変更
    Edge[l].append(r)
UF = UnionFind(N + 1)

for edge_i, edge in enumerate(Edge):  # 同じ端を持つ区間はそのどの端までの数もわかる→それを全て繋いで0とNが繋がっているかで判定
    for edge_j in edge:
        UF.union(edge_i, edge_j)

if UF.same_check(0, N):
    print('Yes')
else:
    print('No')
