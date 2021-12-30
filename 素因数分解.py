from collections import defaultdict


def factorization(n):
    if n == 1:
        return defaultdict(int)
    ret = defaultdict(int)
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

