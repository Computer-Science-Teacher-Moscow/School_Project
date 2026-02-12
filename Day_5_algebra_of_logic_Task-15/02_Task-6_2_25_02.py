# 2.25 №2
from turtle import *

tracer(0)
r = 30
screensize(5000,5000)
rt(30)
for _ in range(3):
    rt(150)
    fd(6 * r)
    rt(30)
    fd(12 * r)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
