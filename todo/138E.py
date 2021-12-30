import sys
from collections import Counter

S = input()
T = input()
S_C = Counter(S)
T_C = Counter(T)
flag = True
A = []
judgenum = 0

for keyt, valuet in T_C.items():
    if keyt not in S_C:
        flag = False
        break
    else:
        values = S_C[keyt]
        a = valuet // values
        b = valuet % values
        A.append((a, b, keyt))
        judgenum = max(a, judgenum)
A.sort(reverse=True)


print(A)