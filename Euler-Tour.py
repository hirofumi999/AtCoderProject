from collections import deque


def euler_tour(G, root):
    n = len(G)
    euler = []
    In = [0] * n
    Out = [0] * n
    Depth = [0] * n
    dq = deque([root])
    dq2 = deque()
    visited = [0] * n
    while dq:
        u = dq.pop()
        if u < 0:
            u = -u
            euler += [-u]
        else:
            euler += [u]
        if visited[u]:
            Out[u] = len(euler) - 1
            continue
        In[u] = len(euler) - 1
        for v in G[u]:
            if visited[v]:
                dq += [-v]
            # [親頂点、子頂点、子頂点、。。。]と入れていく.その後連結
            else:
                dq2 += [v]
                Depth[v] = Depth[u] + 1
        if len(dq2) == 0:
            euler.append(-u)
            Out[u] = len(euler) - 1
        dq.extend(dq2)
        dq2 = deque()
        visited[u] = 1
    return euler, In, Out, Depth
