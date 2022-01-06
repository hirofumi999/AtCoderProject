N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
DP = [float('inf')] * (1 << N)  # bitDP
DP[0] = 0
bit_count = [0]
for _ in range(N):
    bit_count += [x+1 for x in bit_count]

for i in range(1 << N):  # 現在の状態から次に持ってくる数字のidxを考える配るDP
    cnt = 0
    for j in range(N):
        if (i >> j) & 1 == 1:
            cnt += 1
            continue
        DP[i ^ (1 << j)] = min(DP[i ^ (1 << j)], DP[i] + (j - cnt) * Y + abs(A[j] - B[bit_count[i]]) * X)
print(DP[-1])
