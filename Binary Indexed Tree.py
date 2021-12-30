N = int(input())

BIT = [0] * N  # BITを使う


def BIT_query(idx):  # idxまでの合計を返す
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx&(-idx)
    return res_sum


def BIT_update(idx,x):  # idxにxを足す
    while idx <= N:
        BIT[idx] += x
        idx += idx&(-idx)
    return