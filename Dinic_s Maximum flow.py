class MaxFlow:
    def __init__(self, V):
        self.V = V
        self.level = [0] * V
        self.iter = [0] * V
        self.edge = [[] for i in range(V)]

    def add_edge(self, fr, to, cap):
        f, t = len(self.edge[fr]), len(self.edge[to])
        self.edge[fr].append([to, cap, t])
        self.edge[to].append([fr, cap, f])

    def bfs(self, s):
        self.level = [-1] * self.V
        self.level[s] = 0
        Q = []
        Q.append(s)
        while Q:
            v = Q.pop()
            for to, cap, rev in self.edge[v]:
                if cap > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1
                    Q.append(to)

    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(self.edge[v])):
            to, cap, rev = self.edge[v][i]
            if cap > 0 and self.level[v] < self.level[to]:
                d = self.dfs(to, t, min(f, cap))
                if d > 0:
                    self.edge[v][i][1] -= d
                    self.edge[to][rev][1] += d
                    return d
            self.iter[v] = i
        return 0

    def maxFlow(self, s, t, INF=10 ** 8):
        flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0: break
            self.iter = [0] * self.V
            while True:
                f = self.dfs(s, t, INF)
                if f <= 0:
                    break
                flow += f
        return flow


N, M = map(int, input().split())
d = MaxFlow(N)
for i in range(M):
    x, y = map(int, input().split())
    d.add_edge(x, y, 1)
source, sink = map(int, input().split())
print(d.maxFlow(source, sink))
