from collections import defaultdict


def factorization(n):
    global ret
    if n == 1:
        return defaultdict(int)
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            ret[i] += cnt
    if tmp != 1:
        ret[tmp] += 1
    return ret


A, B = map(int, input().split())
mod = 10 ** 9 + 7
ret = defaultdict(int)
for i in range(B + 1, A + 1):
    factorization(i)
ans = 1
for value in ret.values():
    ans *= value + 1
    ans %= mod
print(ans)