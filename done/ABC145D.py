X, Y = map(int, input().split())
mod = 10 ** 9 + 7
Z = Y - X  # Zが行動回数の差
if (X + Y) % 3:  # X + Y は必ず3の倍数になる
    print(0)
    exit()

a_num = ((X + Y) // 3 + Z) // 2
b_num = ((X + Y) // 3 - Z) // 2
#  移動回数が決まれば後はその選び方を求めるのみ

mod = 10 ** 9 + 7
N = a_num + b_num + 1  # N は必要分だけ用意する
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


print(cmb(a_num + b_num, a_num))