Q = int(input())
Query = []
X = []
for _ in range(Q):
    query = tuple(map(int, input().split()))
    Query.append(query)
    X.append(query[1])
X = sorted(list(set(X)))
XtoY = dict()
N = len(X) + 1
BIT = [0] * N


def BIT_query(idx):  # idxまでの合計を返す
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx&(-idx)
    return res_sum


def BIT_update(idx, x):  # idxにxを足す
    while idx <= N:
        BIT[idx] += x
        idx += idx & (-idx)
    return


for i, x in enumerate(X, 1):
    XtoY[x] = i


for query in Query:
    if query[0] == 1:
        BIT_update(XtoY[query[1]], 1)
        continue
    elif query[0] == 2:
        target_num = BIT_query(XtoY[query[1]]) - query[2] + 1
        if target_num <= 0:
            print(-1)
            continue

    else:
        target_num = BIT_query(XtoY[query[1]] - 1) + query[2]
        if target_num > BIT_query(N - 1):
            print(-1)
            continue

    start = 0
    end = N - 1
    while end - start > 1:
        mid = (start + end) // 2
        if BIT_query(mid) < target_num:
            start = mid
        else:
            end = mid
    print(X[end - 1])
