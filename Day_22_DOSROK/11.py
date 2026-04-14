from math import ceil, log2

n = 289
k = 10 + 1015
N = 524_288
i = ceil(log2(k))
V = ceil(n * i * N / 2 ** 23)
print(V)
