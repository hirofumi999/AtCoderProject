def segfunc(x, y):
    return x + y


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        self.n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (self.n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(self.n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def get_tree(self):
        return self.tree[self.num:self.num + self.n]


    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] += x
        self.tree[k] %= mod
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


N = int(input())
mod = 998244353
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [(aa, bb) for aa, bb in zip(A, B)]
AB.sort()
ceil = AB[-1][0]
ans = 0
DP = [0] * (ceil + 1)
DP[0] = 1
ST = SegTree(DP, segfunc, 0)


for i, (max_num, b) in enumerate(AB):
    if max_num >= b:
        ans += ST.query(0, max_num - b + 1) % mod
        ans %= mod
    for num_, value in enumerate(ST.get_tree()[::-1]):
        num = ceil - num_
        if num + b <= ceil:
            ST.update(num + b, value)
print(ans % mod)