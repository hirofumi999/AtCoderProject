from collections import deque

H, W = map(int, input().split())
start_y, start_x = map(int, input().split())
start_y -= 1
start_x -= 1
goat_y, goal_x = map(int, input().split())
goat_y -= 1
goal_x -= 1
Map = [[1 if a == '#' else 0 for a in input()] for _ in range(H)]
Dist = [[float('inf')] * W for _ in range(H)]

Q = deque()
Dist[start_y][start_x] = 0
Q.append((start_y, start_x))

Dy = [1, 0, -1, 0]
Dx = [0, 1, 0, -1]
My = [a for a in range(-2, 3)]
Mx = [a for a in range(-2, 3)]

while Q:
    y, x = Q.popleft()
    if Dist[y][x] >= Dist[goat_y][goal_x]:
        break
    for dy, dx in zip(Dy, Dx):
        ny = dy + y
        nx = dx + x
        if ny < 0 or nx < 0 or ny >= H or nx >= W:
            continue
        if Map[ny][nx]:
            continue
        if Dist[ny][nx] > Dist[y][x]:
            Q.appendleft((ny, nx))
            Dist[ny][nx] = Dist[y][x]
    for dy in My:
        for dx in Mx:
            ny = dy + y
            nx = dx + x
            if ny < 0 or nx < 0 or ny >= H or nx >= W:
                continue
            if Map[ny][nx]:
                continue
            if Dist[ny][nx] > Dist[y][x] + 1:
                Q.append((ny, nx))
                Dist[ny][nx] = Dist[y][x] + 1

print(-1 if Dist[goat_y][goal_x] == float('inf') else Dist[goat_y][goal_x])

