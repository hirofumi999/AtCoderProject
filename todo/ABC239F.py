import heapq


class UnionFind:
    def __init__(self, d):
        n = len(d)
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n
        self.edges = d

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
                self.edges[y] = self.edges[y][:-1]
                self.edges[y].extend(self.edges[x][:-1])
                self.edges[x] = []
            self.par[x] = y
        else:
            if not self.same_check(x, y):
                self.size[x] += self.size[y]
                self.size[y] = 0
                self.edges[x] = self.edges[x][:-1]
                self.edges[x].extend(self.edges[y][:-1])
                self.edges[y] = []
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def siz(self, x):
        x = self.find(x)
        return self.size[x]


N, M = map(int, input().split())
D = list(map(int, input().split()))
if sum(D) != (N - 1) * 2:
    print(-1)
    exit()
for i in range(N):
    D[i] = [i] * D[i]
UF = UnionFind(D)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    UF.union(a, b)

A = []
Ones = []
for i in range(N):
    n = len(UF.edges[i])
    if n == 1:
        Ones.append(UF.edges[i][0])
    elif n >= 2:
        heapq.heappush(A, (-n, UF.edges[i]))
Ans = []
while A and Ones:
    n1, edge1 = heapq.heappop(A)
    edge2 = Ones.pop()
    n = -n1 - 1
    Ans.append((edge1[-1] + 1, edge2 + 1))
    if n == 1:
        Ones.append(edge1[0])
    elif n >= 2:
        heapq.heappush(A, (-n, edge1[:-1]))

if len(Ones) == 2:
    Ans.append((Ones[0] + 1, Ones[1] + 1))
    Ones = []
if A or Ones:
    print(-1)
else:
    for ans in Ans:
        print(*ans)
