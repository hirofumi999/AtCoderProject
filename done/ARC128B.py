def calc(a, b, c):
    if a > b:
        a, b = b, a
    return b


T = int(input())
for _ in range(T):
    r, g, b = map(int, input().split())
    ans = float('inf')
    if r % 3 == g % 3:
        ans = min(ans, calc(r, g, b))
    if r % 3 == b % 3:
        ans = min(ans, calc(r, b, g))
    if g % 3 == b % 3:
        ans = min(ans, calc(g, b, r))
    print(ans if ans != float('inf') else -1)

