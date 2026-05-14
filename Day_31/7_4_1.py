from turtle import *


def f(x, y):
    return (x < A) and (y < 3 * A) or (2 * x + y > 128)


# tracer(0)
# for _ in range(2):
#     fd(10000);
#     bk(20000);
#     fd(10000);
#     rt(90)
# up()
# r = 1
# A = 70
# for x in range(0, 1000, r):
#     for y in range(0, 1000, r):
#         f = (x < A) and (y < 3 * A) or (2 * x + y > 128)
#         if f == 0:
#             goto(x / r, y / r)
#             dot(3, 'red')
# update()
# done()

for A in range(60, 70):
    if all(f(x, y) for x in range(60, 70) for y in range(1, 10)):
        print(A)
        break