import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def num2(x):
    ret = 0
    while x % 2 == 0:
        x //= 2
        ret += 1
    return ret


N, M = map(int, input().split())
A = set(map(int, input().split()))
l = 1
num = -1
for a in A:
    l = lcm(a, l)
    if num < 0:
        num = num2(a)
    elif num != num2(a):
        print(0)
        exit()
start = l // 2
ans = 0
if start <= M:
    M -= start
    ans = 1
    ans += M // l


print(ans)
