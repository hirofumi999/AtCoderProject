N, K = map(int, input().split())
A = list(map(int, input().split()))
Done = [-1] * N
Candy_sum = [-1] * N

start = 0
candy = 0
idx = 1
while True:
    candy += A[start]
    if Done[start] < 0:
        Done[start] = idx
        Candy_sum[start] = candy
        idx += 1
        start = candy % N
    else:
        cycle_start = Done[start]
        cycle_end = idx
        cycle_num = cycle_end - cycle_start
        candies_cycle = candy - Candy_sum[start]
        candies_before_cycle = Candy_sum[start]
        break

if cycle_start >= K:
    for i, done in enumerate(Done):
        if done == K:
            ans = Candy_sum[i]
else:
    ans = Candy_sum[start]
    K -= cycle_start
    cycle = K // cycle_num
    K %= cycle_num
    ans += cycle * candies_cycle
    while K:
        start = ans % N
        ans += A[start]
        K -= 1


print(ans)