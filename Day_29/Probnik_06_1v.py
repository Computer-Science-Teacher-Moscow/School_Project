from turtle import *

tracer(0)
screensize(5000, 5000)
r = 5

for _ in range(8):
    fd(95 * r); rt(135); fd(83 * r); rt(45)

update()
done()