from math import ceil, log2

n = 65
N = 131_072
V = 9 * 2 ** 20
for i in range(1, 1000):
    if ceil(n * i / 8) * N > V:
        print(2 ** (i - 1))
        break
