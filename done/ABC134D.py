N = int(input())
A = [-1] + list(map(int, input().split()))
Ball = [0] * (N + 1)

for i in range(1, N + 1)[::-1]:
    ball = 0
    for j in range(i, N + 1, i):
        ball += Ball[j]
    if A[i] != ball % 2:
        Ball[i] = 1

Ans = []
for i, ball in enumerate(Ball[1:], 1):
    if ball:
        Ans.append(i)
print(len(Ans))
print(*Ans)
