# 2.25 №1
from turtle import *

tracer(0)
r = 30
screensize(5000,5000)
rt(90)
for _ in range(3):
    rt(45)
    fd(10 * r)
    rt(45)
rt(315)
fd(10 * r)
for _ in range(2): rt(90); fd(10 * r)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
