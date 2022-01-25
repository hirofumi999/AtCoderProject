from collections import Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))
Acc = [0]  # 累積和を取る
for a in A:
    Acc.append((Acc[-1] + a) % M)
Calc = Counter(Acc)  # 累積和の値をCounterにいれて、同じ値になるところの数を数え上げる
ans = 0

for acc in Acc:
    Calc[acc] -= 1
    ans += Calc[acc]
print(ans)
