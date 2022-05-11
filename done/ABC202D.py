import sys

sys.setrecursionlimit(10 ** 7)

A, B, K = map(int, input().split())


def combination(n, r):
    ret = 1
    r = min(r, n - r)
    for i in range(r):
        ret *= n - i
        ret //= i + 1
    return ret


def calc(a, b, k, now):
    if a == 0:
        print(now + 'b' * b)
        exit()
    if b == 0:
        print(now + 'a' * a)
        exit()
    choice_a = combination(a + b - 1, b)
    if k <= choice_a:
        return calc(a - 1, b, k, now + 'a')
    else:
        return calc(a, b - 1, k - choice_a, now + 'b')

calc(A, B, K, "")