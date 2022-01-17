N = int(input())
f = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
X = list(map(int, input().split()))
base = 0
ma = float('inf')
mi = -float('inf')
for a_, t in f:
    if t == 1:
        base += a_
    elif t == 2:
        a = a_ - base
        mi = max(mi, a)
        if ma < mi:
            ma = mi
    else:
        a = a_ - base
        ma = min(ma, a)
        if ma < mi:
            mi = ma

for x in X:
    if x >= ma:
        print(ma + base)
    elif x <= mi:
        print(mi + base)
    else:
        print(x + base)