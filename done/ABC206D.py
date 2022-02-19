
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


N = int(input())
A = list(map(int, input().split()))
UF = UnionFind(max(A) + 1)
ans = 0
for a1, a2 in zip(A, A[::-1]):
    if UF.same_check(a1, a2):
        continue
    else:
        UF.union(a1, a2)
        ans += 1
print(ans)
