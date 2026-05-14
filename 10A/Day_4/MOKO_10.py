from turtle import *

tracer(0)
# screensize(5000,5000)
r = 25
lt(90)
for _ in range(3):
    fd(12 * r); lt(270); bk(10 * r); rt(90)
up()
fd(6 * r)
rt(90)
bk(4 * r)
lt(90)
down()
for _ in range(4):
    fd(16 * r)
    rt(270)
    fd(8 * r)
    rt(270)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x * r, y * r)
        dot(3,'red')
update()
done()

