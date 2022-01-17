import sys

sys.setrecursionlimit(10 ** 6)

H, W, A, B = map(int, input().split())

Map = [[0] * W for _ in range(H)]
ans = 0


def calc(num, start_num=0):
    global ans
    if num == A:
        ans += 1
        return
    for i in range(start_num, H * W):
        y = i // W
        x = i % W
        if Map[y][x]:
            continue
        if y < H - 1 and not (Map[y+1][x]):
            Map[y][x] = 1
            Map[y + 1][x] = 1
            calc(num + 1, i + 1)
            Map[y][x] = 0
            Map[y + 1][x] = 0
        if x < W - 1 and not (Map[y][x+1]):
            Map[y][x] = 1
            Map[y][x+1] = 1
            calc(num + 1, i + 1)
            Map[y][x] = 0
            Map[y][x+1] = 0


calc(0)
print(ans)

