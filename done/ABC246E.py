from collections import deque
from sys import stdin

N = int(input())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
S = [[-1 if a == '#' else float('inf') for a in stdin.readline()[:-1]] for _ in range(N)]
S[sy - 1][sx - 1] = 0

if (sy + sx) % 2 != (gy + gx) % 2:
    print(-1)
    exit()

Q = deque()
Q.append((sy - 1, sx - 1))

while Q:
    y, x = Q.popleft()
    for dy, dx in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
        cnt = 1
        while True:
            ny = y + cnt * dy
            nx = x + cnt * dx
            if ny == gy - 1 and nx == gx - 1:
                print(S[y][x] + 1)
                exit()
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                break
            if S[ny][nx] == -1:
                break
            if S[ny][nx] > S[y][x] + 1:
                S[ny][nx] = S[y][x] + 1
                Q.append((ny, nx))
            cnt += 1
print(-1)