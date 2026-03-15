from functools import lru_cache


@lru_cache(None)
def g(n):
    if n < 10: return 2 * n
    return g(n - 2) + 1


def f(n):
    return 2 * (g(n - 3) + 8)


for i in range(9, 16600): f(i)

print(f(15548))
