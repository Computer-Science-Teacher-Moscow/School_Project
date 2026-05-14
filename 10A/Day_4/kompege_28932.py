from math import ceil, log2

n = 257
k = 17 + 4080
i = ceil(log2(k))
v = ceil(i * n / 8)
N = 8_388_608
V = v * N / 2 ** 20
print(V)
