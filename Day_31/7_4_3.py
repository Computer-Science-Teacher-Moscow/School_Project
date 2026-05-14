from turtle import *


def f(x, y):
    return (x * y > A) or (x > y) or (11 > x)


tracer(0)
for _ in range(2):
    fd(10000);
    bk(20000);
    fd(10000);
    rt(90)
up()
r = 1
A = 130
for x in range(0, 1000, r):
    for y in range(0, 1000, r):
        q = (x * y > A) or (x > y) or (11 > x)
        if q == 0:
            goto(x * 5, y *5)
            dot(3, 'red')
update()
done()

# for A in range(125, 0,-1):
#     if all(f(x, y) for x in range(10, 13) for y in range(10, 13)):
#         print(A)
#         break
