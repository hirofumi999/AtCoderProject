N = int(input())
K = int(input())
Wall = [[1 if a == '#' else 0 for a in input()] for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0


def dfs(num):
    global ans
    if num == K:
        ans += 1
        return
    nex = set()
    for i in range(N):
        for j in range(N):
            if Wall[i][j] != 2:
                continue
            for ii, jj in zip(dy, dx):
                ni = i + ii
                nj = j + jj
                if ni < 0 or nj < 0 or ni >= N or nj >= N:
                    continue
                if Wall[ni][nj]:
                    continue
                nex.add((ni, nj))
    for ni, nj in nex:
        Wall[ni][nj] = 2
        dfs(num + 1)
        Wall[ni][nj] = 1
    for ni, nj in nex:
        Wall[ni][nj] = 0


for i in range(N):
    for j in range(N):
        if Wall[i][j]:
            continue
        Wall[i][j] = 2
        dfs(1)
        Wall[i][j] = 1
print(ans)