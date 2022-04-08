N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]
B = [0] * (M + 1)


for bi in range(M + 1):
    bi_num = C[bi]
    for ai in range(1, bi + 1):
        if ai > N:
            continue
        bi_num -= A[ai] * B[bi - ai]
    bi_num //= A[0]
    B[bi] = bi_num

print(*B[::-1])