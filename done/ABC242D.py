import sys

sys.setrecursionlimit(10 ** 6)

S = input()
Q = int(input())
query = [tuple(map(int, input().split())) for _ in range(Q)]


def calc(t, k):
    if t == 0:
        return S[k]
    if k == 0:
        ret = (ord(S[0]) - ord('A') + t) % 3
        return chr(ord('A') + ret)
    ret = (ord(calc(t - 1, k // 2)) - ord('A')) + k % 2 + 1
    return chr(ret % 3 + ord('A'))


for t, k in query:
    k -= 1
    print(calc(t, k))
