from functools import lru_cache
from time import time
from fractions import Fraction



@lru_cache(1000)
def g(n):
    if n < 31: return 4
    return Fraction(n , 2) * g(n - 2)


@lru_cache(3)
def f(n):
    if n < 14: return 8 * (g(n - 3))
    return n * f(n - 1)


print('Start calulate G:')
start_time = time()
for i in range(30, 641451):
    if i % 10_000 == 0: print(i)
    g(i)
print('End calulate G:')

print('Start calulate F:')
for i in range(13, 320727):
    if i % 10_000 == 0: print(i)
    f(i)
end_time = time()
print('End calulate F:')
print(f'Time calculation = {end_time - start_time}')


print(f(320726) // g(641450))
