N = int(input())
P = list(map(int, input().split()))
num = 0
Ans = []
tmp = []
for i in range(N - 1):
    cnt = 0
    tmp.append(i + 1)
    if P[i] > P[i + 1]:
        for t in tmp[::-1]:
            P[t - 1], P[t] = P[t], P[t - 1]
            Ans.append(t)
        tmp = []
if P == [a for a in range(1, N + 1)] and len(Ans) == N - 1:
    for ans in Ans:
        print(ans)
else:
    print(-1)
