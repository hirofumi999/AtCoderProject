N, K = map(int, input().split())
A = list(map(int, input().split()))
Plus = []
Minus = []
p = 0
m = 0
z = 0

for a in A:
    if a > 0:
        Plus.append(a)
        p += 1
    elif a < 0:
        Minus.append(a)
        m += 1
    else:
        z += 1

M = m * p
P = p * (p-1) // 2 + m * (m-1) // 2
Z = z * (p + m) + z * (z-1) // 2

if K <= M:
    Plus.sort()
    Minus.sort(reverse=True)


elif K <= M + Z:
    print(0)
else:
     K -= M + Z
