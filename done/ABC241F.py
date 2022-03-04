from collections import defaultdict, deque
from bisect import bisect_left

H, W, N = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

X = defaultdict(list)
Y = defaultdict(list)

for _ in range(N):
    y, x = map(int, input().split())
    X[x].append(y)
    Y[y].append(x)

for key in X.keys():
    X[key].sort()
for key in Y.keys():
    Y[key].sort()

Q = deque()
Q.append([sy, sx])
Done = dict()
Done[(sy, sx)] = 0
while Q:
    y, x = Q.popleft()
    if y == gy and x == gx:
        print(Done[(y, x)])
        exit()
    idx_x = bisect_left(X[x], y)
    if idx_x >= 1:
        ny = X[x][idx_x - 1] + 1
        nx = x
        if (ny, nx) not in Done:
            Done[(ny, nx)] = Done[(y, x)] + 1
            Q.append([ny, nx])
    if idx_x < len(X[x]):
        ny = X[x][idx_x] - 1
        nx = x
        if (ny, nx) not in Done:
            Done[(ny, nx)] = Done[(y, x)] + 1
            Q.append([ny, nx])
    idx_y = bisect_left(Y[y], x)
    if idx_y >= 1:
        ny = y
        nx = Y[y][idx_y - 1] + 1
        if (ny, nx) not in Done:
            Done[(ny, nx)] = Done[(y, x)] + 1
            Q.append([ny, nx])
    if idx_y < len(Y[y]):
        ny = y
        nx = Y[y][idx_y] - 1
        if (ny, nx) not in Done:
            Done[(ny, nx)] = Done[(y, x)] + 1
            Q.append([ny, nx])

print(-1)