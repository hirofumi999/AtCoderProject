K, N, M = map(int, input().split())
A = list(map(int, input().split()))
B = []
A_B = []
for i, a in enumerate(A):
    B.append(int(a * M / N))
    A_B.append(((A[i] * M - B[i] * N), i))
M -= sum(B)
A_B.sort(reverse=True)
for _, i in A_B:
    if M:
        M -= 1
        B[i] += 1
    else:
        break

print(*B)