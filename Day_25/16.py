from sys import setrecursionlimit
setrecursionlimit(30000)
# from functools import lru_cache
from fractions import Fraction


# @lru_cache(1000)
def g(n):
    if n >= 22560: return Fraction(n,23) + 33
    return g(n + 11) - 4


# @lru_cache(1000)
def f(n):
    if n < 21: return 10 * (g(n - 7) - 36)
    return f(n - 8) + 1095

# for i in range(22560, 0,-1): g(i)
# for i in range(20, 548): f(i)

print(f(548))
