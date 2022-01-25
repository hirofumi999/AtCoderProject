N, K = map(int, input().split())
D = N * K
A = list(map(int, input().split()))
Wait = dict()
First = dict()
Nex = [-1] * N
for i, a in enumerate(A):
    if a in Wait:
        Nex[Wait.pop(a)] = i + 1
        Wait[a] = i
    else:
        Wait[a] = i
        if a not in First:
            First[a] = i

for key, value in Wait.items():
    Nex[value] = First[key] + 1 + N

now = 0
Done = [-1] * N
Done[0] = 0  # cycle
ans = 0
while True:
    nex = Nex[now]
    distance = nex - now
    if distance > D:
        ans = A[now:]
        break
    else:
        D -= distance
    if Done[nex % N] >= 0:
        cycle_start = Done[nex % N]
        cycle_end = Done[now] + Nex[now] // N
        D %= (cycle_end - cycle_start) * N
        now = nex % N
        break
    else:
        Done[nex % N] = Done[now] + Nex[now] // N
        now = nex % N

if D == 0:
    print('')
    exit()
while True:
    if ans:
        Ans = ans
        break
    nex = Nex[now]
    distance = nex - now
    if distance > D:
        Ans = A[now:]
        break
    else:
        D -= distance
        now = nex % N

W = dict()
p = []
idx = -1
for ans in Ans:
    idx += 1
    p.append(ans)
    if ans in W:
        idx = W.pop(ans)
        if idx + 1 < len(p):
            for i in p[idx + 1: -1]:
                W.pop(i)
        p = p[:idx]
        idx -= 1
    else:
        W[ans] = idx
print(*p)