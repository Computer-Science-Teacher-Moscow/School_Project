from math import ceil
n = 2468
N = 4_635_815
V = 10 * 2 ** 30
for i in range(1, 1000):
    if ceil(i * n / 8) * N  >= V:
        print(2 ** (i-1) + 1)
        break