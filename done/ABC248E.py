N, K = map(int, input().split())
Points = [tuple(map(int, input().split())) for _ in range(N)]

if K == 1:
    print('Infinity')
    exit()
Ans = set()
for idx1, (x1, y1) in enumerate(Points):
    for idx2, (x2, y2) in enumerate(Points[:idx1]):
        cnt = [idx1, idx2]
        for idx3, (x3, y3) in enumerate(Points):
            if idx1 == idx3 or idx2 == idx3:
                continue
            if (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1) == 0:
               cnt.append(idx3)
        if len(cnt) >= K:
            Ans.add(tuple(sorted(cnt)))
print(len(Ans))

