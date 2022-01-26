import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
A = [[0] * 2 * N for _ in range(2 * N)]
for i in range(2 * N - 1):
    aa = list(map(int, input().split()))
    for j, a in enumerate(aa, i + 1):
        A[i][j] = a

Done = [0] * (2 * N)
ans = 0


def calc(done, a=0):
    global ans
    if sum(done) == 2 * N:
        ans = max(ans, a)
        return 0
    for i, do in enumerate(done):
        if do:
            continue
        done[i] = 1
        for j in range(i + 1, 2 * N):
            if done[j] == 1:
                continue
            done[j] = 1
            calc(done, a ^ A[i][j])
            done[j] = 0
        done[i] = 0
        break


calc(Done)
print(ans)




