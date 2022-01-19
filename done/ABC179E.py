
def calc(*args):
    N, X, M = args
    ans = 0
    done = dict()
    acc = [0]
    for i in range(N):
        ans += X
        if X in done:
            circle_num = i - done[X]
            rest = N - done[X]
            rest_circle = rest // circle_num
            rest_rest = rest % circle_num + done[X]
            circle_sum = ans - acc[done[X] + 1]
            ans = circle_sum * rest_circle + acc[rest_rest]
            break
        else:
            done[X] = i
            acc.append(ans)
        X = pow(X, 2, M)
    return ans

def main():
    N, X, M = map(int, input().split())
    print(calc(N, X, M))


if __name__ == '__main__':
    main()