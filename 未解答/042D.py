import sys
#input = sys.stdin.buffer.readline


H, W, A, B = map(int, input().split())
mod = 10**9 + 7
ans = 1
a = min(W-B-1, H-1)
for i in range(1,a+1):
    ans *= (W-B-1+H-i-1)//i
    ans %= mod
C1 = 1
C2 = ans
for i in range(1, H-A+1):
    ans += C1 * (B+i-1) * pow(i, mod-2, mod) * C2 * (H-i) * pow(W-B-1+H-i-1, mod-2, mod)
    ans %= mod
print(ans)