import random


def solve(*args):
    n, A = args
    return n


def solve_jury(*args):
    n, A = args
    return A


def random_list_generator(n, mi=0, ma=10**6):
    return [random.randint(mi, ma) for _ in range(n)]


def random_int_generator(mi=1, ma=10):
    return random.randint(mi, ma)


def main():
    check_num = 1000
    for t in range(check_num):
        n = random_int_generator()
        A = random_list_generator(n, 0, 10 ** 6)
        ans1 = solve(n, A)
        ans2 = solve_jury(n, A)
        if ans1 != ans2:
            print(f'Wrong Answer on Test {t}')
            print(f'{ans1=}, {ans2=}')
    return 0




if __name__ == '__main__':
    main()
