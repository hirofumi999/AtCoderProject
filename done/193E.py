def ext_gcd(a, b):
    """
    ap + bq = gcd(a, b)となる(p, q)を求め、d, p, qを返す
    :param a:
    :param b:
    :return:
    """
    if b:
        d, q, p = ext_gcd(b, a % b)
        q -= (a // b) * p
        return d, p, q
    return a, 1, 0


def chinese_rem(num, mod_lst):
    """
    :param num: list
    :param mod_lst: list
    :return: x = r (mod m)の (r, m) 解なしの場合は(0, -1)
    """
    r = 0
    m = 1
    for i in range(len(num)):
        d, p, q = ext_gcd(m, mod_lst[i])
        if (num[i] - r) % d != 0:
            return 0, -1
        tmp = (num[i] - r) // d * p % (mod_lst[i] // d)
        r += m * tmp
        m *= mod_lst[i] // d
    return r % m, m


T = int(input())
for _ in range(T):
    X, Y, P, Q = map(int, input().split())
    ans = float('inf')
    for y in range(Y):
        for q in range(Q):
            r, m = chinese_rem([X + y, P + q], [2 * X + 2 * Y, P + Q])
            if m == -1:
                continue
            ans = min(ans ,r)
    print(ans if ans != float('inf') else 'infinity')
