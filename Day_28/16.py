from functools import lru_cache
from fractions import Fraction
from time import time


@lru_cache(1000)
def G(n):
    if n < 51: return 4
    return Fraction(n, 2) * G(n - 2)


@lru_cache(3)
def F(n):
    if n < 10: return 8 * G(n - 3)
    return n * F(n - 1)

stat_time = time()
print('Начинаем вычислять G')

for i in range(50, 641450):
    if i % 10_000 == 0: print(i)
    G(i)
print('Закончили вычислять G')
print('Начинаем вычислять F')
for i in range(9, 320726):
    if i % 10_000 == 0: print(i)
    F(i)
print('Закончили вычислять F')


print(F(320725)/G(641448))
end_time = time()
print(f'Время вычислений равно {end_time - stat_time}')
