from turtle import *


tracer(0)
screensize(5000, 5000)
r = 40
# lt(90)

rt(315)
for _ in range(7):
    fd(12 * r)
    rt(45)
    fd(6 * r)
    rt(135)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
