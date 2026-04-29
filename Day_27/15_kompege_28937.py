from fractions import Fraction
from functools import lru_cache


@lru_cache(100)
def g(n):
    if n >= 22560: return Fraction(n, 23) + 33
    return g(n + 11) - 4


# @lru_cache(None)
def f(n):
    if n < 21: return 10 * (g(n - 7) - 36)
    return f(n - 8) + 1095

for i in range(22560, 0,-1): g(i)
# for i in range(20, 1000): f(i)


print(f(548))