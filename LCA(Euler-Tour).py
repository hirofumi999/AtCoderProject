import sys

sys.setrecursionlimit(10**6)


class LCAEulerTour:
    """
    グラフ情報からEuler-Tourを実施し、LCAを構築
    Treeは1-index
    他は0-index
    """

    def __init__(self, n, graph, root=0):
        self.n = n
        self.First = [-1] * n
        self.depth = [0] * n
        self.EulerTour = self._init_eulertour(graph, root)
        self.num = 1 << (len(self.EulerTour) - 1).bit_length()
        self.tree = [(n, n)] * 2 * self.num
        for i, v in enumerate(self.EulerTour):
            self.tree[self.num + i] = (self.depth[v], v)
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def _init_eulertour(self, graph, root):
        def dfs(v, d):
            self.First[v] = len(ET)
            self.depth[v] = d
            ET.append(v)
            for w in graph[v]:
                if self.First[w] >= 0:
                    continue
                dfs(w, d + 1)
                ET.append(v)
        ET = []
        dfs(root, 0)
        return ET

    def query(self, l, r): # 閉区間
        res = (self.n, self.n)
        l = self.First[l]
        r = self.First[r]
        if r < l:
            r, l = l, r
        l += self.num
        r += self.num + 1
        while l < r:
            if l & 1:
                res = min(res, self.tree[l])
                l += 1
            if r & 1:
                res = min(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res[1]
