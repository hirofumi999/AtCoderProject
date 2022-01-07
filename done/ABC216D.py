import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
Now_idx = [0] * (M + 1)
Goal_idx = [0]
A = [[]]
Top = defaultdict(int)


def push(column_num):
    in_column_idx = Now_idx[column_num]
    if in_column_idx < Goal_idx[column_num]:
        color = A[column_num][in_column_idx]
        if Top[color] != 0:
            same_color_column_num = Top[color]
            Now_idx[same_color_column_num] += 1
            Top[color] = 0
            push(same_color_column_num)
            Now_idx[column_num] += 1
            push(column_num)
        else:
            Top[color] = column_num
            return
    else:
        return


for i in range(1, M + 1):
    k = int(input())
    Goal_idx.append(k)
    A.append(list(map(int, input().split())))
    push(i)

if Now_idx == Goal_idx:
    print('Yes')
else:
    print('No')

