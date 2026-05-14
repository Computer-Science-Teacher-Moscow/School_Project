from turtle import *


def f(x, y):
    return (x * y < A) or (5 * x < y) or (486 <= x)


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

for A in range(1125000, 2000000):
    if all(f(x, y) for x in range(480, 490) for y in range(2400, 2500)):
        print(A)
        break
