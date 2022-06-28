N = int(input())
A = list(map(int, input().split()))
flag = 0

end = N - 1
start = 0

while start <= end:
    while start <= end and A[end] == flag:
        end -= 1
    if start > end:
        print('Yes')
        exit()
    if A[start] == flag:
        start += 1
        flag = 1 - flag
    else:
        print('No')
        exit()

if start <= end:
    print('Yes')
