from functools import lru_cache
from fractions import Fraction

@lru_cache(100)
def f(n):
    if n < 10: return 3
    return (n + 4) * f(n - 5)

for i in range(9, 257487): f(i)

print((Fraction(f(257487),683) + 67 * f(257477)) / f(257472))
