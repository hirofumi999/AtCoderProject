
N = 10**6
bit_count = [0]
for _ in range(N):
    bit_count += [x+1 for x in bit_count]
print(bit_count)