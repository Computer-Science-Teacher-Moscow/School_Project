# def get_r(n: int):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r += '10'
#     else:
#         r = '1' + r + '00'
#     return int(r, 2)
#
# for num in range(1, 1000):
#     if get_r(num) > 107:
#         print(num)
#         break

# from functools import lru_cache
# from fractions import Fraction
#
#
# @lru_cache()
# def f(n):
#     if n == 1: return 1
#     return n * f(n - 1)
#
#
# for i in range(1, 2025): f(i)
# print((Fraction(f(2025), 25) + f(2024)) / f(2023))

# size = 1024 * 280
# V = 280 * 2 ** 13
# for i in range(1, 1000):
#     if size * (i + 3) == V:
#         print(2 ** i)
#         break

# from itertools import product
#
# word = ''.join(sorted('ВЕСНА'))
# for i, pr in enumerate(product(word, repeat = 4), 1):
#     w = ''.join(pr)
#     if 'Е' not in w and 'АА' not in w:
#         print(i)

from ipaddress import ip_network, ip_address
