mod = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]


def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return (fact[n] * factinv[r] % mod) * factinv[n - r] % mod


for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


print(cmb(n, r))