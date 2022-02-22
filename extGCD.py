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
