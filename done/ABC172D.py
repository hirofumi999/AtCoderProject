N = int(input())
ans = 0
for i in range(1, N + 1):  # 約数側から考える
    num = N // i
    ans += (i + num * i) * num // 2
print(ans)
