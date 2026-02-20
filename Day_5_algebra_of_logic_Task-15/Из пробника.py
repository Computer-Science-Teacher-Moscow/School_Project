# Из пробника
from turtle import *

tracer(0)
r = 30
screensize(5000, 5000)

fd(5 * r)
for _ in range(6):
    fd(23 * r)
    rt(45)
    fd(17 * r)
    rt(135)
lt(90)
fd(7 * r)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
