def moebius_table(n):
    p = [a for a in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if p[i] == i:
            for j in range(i ** 2, n + 1, i):
                p[j] = i
            for j in range(i ** 2, n + 1, i ** 2):
                p[j] = 0
    ret = [0] * (n + 1)
    ret[1] = 1
    for i in range(2, n + 1):
        ret[i] = (p[i] and -ret[i // p[i]])
    return ret


if __name__ == '__main__':
    print(moebius_table(20))