N = int(input())
S = [int(a) for a in input()]
T = [int(a) for a in input()]
A = []
for s, t in zip(S, T):
    if s == t:
        if s == 0:
            A.append(0)
    else:
        A.append(s - t)
if sum(A) != 0:
    print(-1)
    exit()

ans = 0
tmp = 0
for a in A:
    tmp += a
    if a == 1:
        ans += 1
    elif a == 0:
        if tmp == 0:
            continue
        else:
            ans += 1


print(ans)