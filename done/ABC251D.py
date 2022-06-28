W = int(input())
Ans = []

for i in range(1, 100):
    Ans.append(i)
    Ans.append(i * 100)
    Ans.append(i * 10000)

Ans.sort()

for i in range(len(Ans)):
    if Ans[i] > W:
        Ans = Ans[:i]
        break

print(len(Ans))
print(*Ans)