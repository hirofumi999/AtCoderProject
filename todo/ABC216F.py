import heapq

def segfunc1(x,y):
    return x+y
class LazySegTree_RAQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [0]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v==0:
                continue
            self.lazy[i] = 0
            self.lazy[2*i] += v
            self.lazy[2*i+1] += v
            self.tree[2*i] += v
            self.tree[2*i+1] += v
    def add(self,l,r,x):
        ids = self.gindex(l,r)
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] += x
                self.tree[l] += x
                l += 1
            if r&1:
                self.lazy[r-1] += x
                self.tree[r-1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1]) + self.lazy[i]
    def query(self,l,r):
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res


N, M = map(int, input().split())
Range = []
for i in range(M):
    l, r, x = map(int, input().split())
    l -= 1
    Range.append((l, r, x))
Range.sort()
MustStart = []
for _, e, x in Range:
    MustStart.append((e - x))
ST = LazySegTree_RAQ(MustStart, segfunc1, 0)

Ans = [0] * N
A = []
idx = 0
while idx < M:
    start, end, x = Range[idx]
    heapq.heappush(A, (end - x, idx))
    idx += 1
    if idx == M:
        break
    nex, i = heapq.heappop(A)
    if Range[idx][0] > nex:
        must_start = ST.query(i, i + 1)
        num = Range[i][1] - must_start
        if num <= 0:
            continue
        for one in range(must_start, Range[i][1]):
            Ans[one] = 1
        ST.add(0, idx, num)
    else:
        heapq.heappush(A, (nex, i))

while A:
    nex, i = heapq.heappop(A)
    must_start = ST.query(i, i + 1)
    num = Range[i][1] - must_start
    if num <= 0:
        continue
    for one in range(must_start, Range[i][1]):
        Ans[one] = 1
    ST.add(0, idx, num)

print(Ans)