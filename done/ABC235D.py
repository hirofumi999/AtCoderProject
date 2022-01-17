from collections import deque

a, N = map(int, input().split())


Done = {N}
Num = dict()
Q = deque()
Q.append(N)
Num[N] = 0

while Q:
    now = Q.popleft()
    if now == 1:
        print(Num[now])
        exit()
    if now % a == 0:
        nex = now // a
        if nex not in Done:
            Q.append(nex)
            Done.add(nex)
            Num[nex] = Num[now] + 1
    now = str(now)
    if len(now) >= 2 and now[-1] != '0' and now[1] != '0':
        nex = int(now[1:]) * 10 + int(now[0])
        if nex not in Done:
            Q.append(nex)
            Done.add(nex)
            Num[nex] = Num[int(now)] + 1
print(-1)