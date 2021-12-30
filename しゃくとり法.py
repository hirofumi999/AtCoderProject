# lからrの範囲でのしゃくとり法。和がK以下

ans = 0
end = 0
tmp = 0
for start in range(N):
    while end < N and tmp+A[end] < K:
        tmp += A[end]
        end += 1
    tmp -= A[start]
    ans += end - start
