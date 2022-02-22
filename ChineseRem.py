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


if __name__ == '__main__':
    print(chinese_rem([3, 4], [5, 7]))
