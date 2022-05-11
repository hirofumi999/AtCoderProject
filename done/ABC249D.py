from collections import Counter

N = int(input())
A = list(map(int, input().split()))
CA = Counter(A)

ans = CA[0] ** 2 * (N - CA[0])

for key, value in CA.items():
    if key == 0:
        continue
    for i in range(1, int(key**0.5)+1):
        if key % i == 0:
            j = key // i
            if i == j:
                ans += value * CA[i] * CA[j]
            else:
                ans += 2 * value * CA[i] * CA[j]
print(ans)