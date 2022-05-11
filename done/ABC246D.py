N = int(input())
x = int(N ** (1/3)) + 10


def calc(a, b):
    c = a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3
    return c >= N


ans = float('inf')
if N == 0:
    ans = 0
for i in range(x):
    if i ** 3 >= N:
        ans = min(ans, i ** 3)
        break
    start = -1
    end = 10 ** 7
    while end - start > 1:
        mid = (start + end) // 2
        if calc(i, mid):
            end = mid
        else:
            start = mid
    ans = min(ans, i ** 3 + i ** 2 * end + i * end ** 2 + end ** 3)

print(ans)


