X = input()
N = len(X)
a = int(X[0])
X = int(X)
ans = float('inf')

for i in range(10):
    cnt1 = 0
    for j in range(N):
        cnt1 *= 10
        if a + i * j < 10:
            cnt1 += a + i * j
        else:
            break
    else:
        if cnt1 >= X:
            ans = min(ans, cnt1)
for i in range(10):
    cnt2 = 0
    for j in range(N):
        cnt2 *= 10
        if a - i * j >= 0:
            cnt2 += a - i * j
        else:
            break
    else:
        if cnt2 >= X:
            ans = min(ans, cnt2)

a += 1
if a == 10:
    a = 1
    N += 1

for i in range(10):
    cnt1 = 0
    for j in range(N):
        cnt1 *= 10
        if a + i * j < 10:
            cnt1 += a + i * j
        else:
            break
    else:
        if cnt1 >= X:
            ans = min(ans, cnt1)
for i in range(10):
    cnt2 = 0
    for j in range(N):
        cnt2 *= 10
        if a - i * j >= 0:
            cnt2 += a - i * j
        else:
            break
    else:
        if cnt2 >= X:
            ans = min(ans, cnt2)

print(ans)