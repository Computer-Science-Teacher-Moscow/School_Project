from turtle import *


def f(x, y):
    return (78125 != y + 4*x) or (A > x) and (A > y)


# tracer(0)
# for _ in range(2):
#     fd(10000);
#     bk(20000);
#     fd(10000);
#     rt(90)
# up()
# r = 1
# A = 40
# for x in range(0, 1000, r):
#     for y in range(0, 1000, r):
#         q = (5 < y) or (x > 32) or (x + 2 * y < A)
#         if q == 0:
#             goto(x * 10, y *10)
#             dot(3, 'red')
# update()
# done()

for A in range(78121,100000):
    if all(f(x, y) for x in range(1, 10) for y in range(78000, 79000)):
        print(A)
        break
