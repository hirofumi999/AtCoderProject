import math


def calc_dist(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


N = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())


y = 0
x = 0
ds = 360 / N
for i in range(N // 2):
    dx = math.cos(math.radians(ds * i))
    dy = math.sin(math.radians(ds * i))
    x += dx
    y += dy

one_dist = calc_dist(x0, x1, y0, y1) / calc_dist(x, 0, y, 0)
deg = math.atan2(y1 - y0, x1 - x0) - math.atan2(y, x)


print(x0 + one_dist * math.cos(deg), y0 + one_dist * math.sin(deg))

