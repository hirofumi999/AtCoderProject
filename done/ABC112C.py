N = int(input())
Points = [tuple(map(int, input().split())) for _ in range(N)]
Points.sort(key=lambda x: x[2], reverse=True)
for cx in range(101):
    for cy in range(101):
        ch = -1
        flag = True
        for i, (x, y, h) in enumerate(Points):
            d = abs(cx - x) + abs(y - cy)
            if i == 0:
                ch = d + h
                continue
            if max((ch - d), 0) != h:
                flag = False
                break
        if flag:
            print(cx, cy, ch)
            exit()

