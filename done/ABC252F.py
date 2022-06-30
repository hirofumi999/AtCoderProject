import heapq

N, L = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
if L > sum(A):
    A.append(L - sum(A))
heapq.heapify(A)


while len(A) > 1:
    first = heapq.heappop(A)
    second = heapq.heappop(A)
    ans += first + second
    heapq.heappush(A, first + second)

print(ans)