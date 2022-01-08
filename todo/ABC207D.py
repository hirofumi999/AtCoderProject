N = int(input())
A_ = [tuple(map(int, input().split())) for _ in range(N)]
A = [(0, 0, 0)]
DistA = []
for i in range(1, N):
    A.append(((A_[i][1] - A_[0][1]) ** 2 + (A_[i][0] - A_[0][0]) ** 2, A_[i][0] - A_[0][0], A_[i][1] - A_[0][1]))
A.sort()
B_ = [tuple(map(int, input().split())) for _ in range(N)]
for i in range(N):
    B = [(0, 0, 0)]
    for j in range(N):
        if i == j:
            continue
        B.append(((B_[i][0] - B_[j][0]) ** 2 + (B_[i][1] - B_[j][1]) ** 2, B_[j][0] - B_[i][0], B_[j][1] - B_[i][1]))
    B.sort()
    if N == 1:
        print('Yes')
        exit()
    elif N == 2:
        if B[1][0] == A[1][0]:
            print('Yes')
            exit()
        else:
            print('No')
            exit()
    flag = False
    for a, b in zip(A, B):
        if a[0] != b[0]:
            flag = True
            break
    if flag:
        continue
    dista, ax1, ay1 = A[1][0], A[1][1], A[1][2]
    ProA = []
    ProAA = []
    for j in range(2, N):
        ProA.append(ax1 * A[j][1] + ay1 * A[j][2])
        ProAA.append(ax1 * A[j][2] - ay1 * A[j][1])
    for j in range(1, N):
        distb, bx1, by1 = B[j][0], B[j][1], B[j][2]
        if distb > dista:
            break
        ProB = []
        ProBB = []
        for k in range(1, N):
            if j == k:
                continue
            ProB.append(bx1 * B[k][1] + by1 * B[k][2])
            ProBB.append(bx1 * B[k][2] - by1 * B[k][1])
        if ProB == ProA and ProBB == ProAA:
            print('Yes')
            exit()
print('No')


