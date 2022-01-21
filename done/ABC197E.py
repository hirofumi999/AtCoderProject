N = int(input())
Balls_ = [tuple(map(int, input().split())) for _ in range(N)]
Balls_.sort(key=lambda x: x[1])
Balls = []
now = -1
tmp = []
for x, c in Balls_:
    if c != now:
        now = c
        if tmp:
            Balls.append(tmp)
        tmp = [x]
    else:
        tmp.append(x)
if tmp:
    Balls.append(tmp)

DP = dict()
DP[0] = 0

for balls in Balls:
    ma = max(balls)
    mi = min(balls)
    dp = dict()
    for start, dist in DP.items():
        if ma in dp:
            dp[ma] = min(abs(start - mi) + (ma - mi) + dist, dp[ma])
        else:
            dp[ma] = abs(start - mi) + (ma - mi) + dist
        if mi in dp:
            dp[mi] = min(dp[mi], abs(start - ma) + (ma - mi) + dist)
        else:
            dp[mi] = abs(start - ma) + (ma - mi) + dist
    DP = dp
ans = float('inf')

for start, dist in DP.items():
    ans = min(ans, dist + abs(start))
print(ans)