from math import dist
from turtle import *
from random import random
from itertools import combinations
from statistics import mean

clusters = []
data = []
with open('10_8_13-14_27A.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        data.append((x, y))

while data:
    kl = [data.pop()]
    for point in kl:
        sosed = [p for p in data if dist(point, p) < 1]
        for p1 in sosed:
            kl.append(p1)
            data.remove(p1)
    clusters.append(kl)
print(*(len(kl) for kl in clusters))


# tracer(0)
# screensize(5000, 5000)
# r = 10
# up()
# for kl in clusters:
#     color = random(), random(), random()
#     for x, y in kl:
#         goto(x * r, y * r)
#         dot(3, color)
# update()
# mainloop()

def get_extreme_points():
    res = []
    for kl_a, kl_b in combinations(clusters, 2):
        print(len(kl_b), len(kl_b))
        res_1 = []
        for point in kl_a:
            min_dist = min((dist(point, p), (point, p)) for p in kl_b)
            res_1.append(min_dist)
        res.append(min(res_1)[1])
    return tuple(res)


# extreme_points = get_extreme_points()
# print(extreme_points)
extreme_points = set(point for points in get_extreme_points() for point in points)
print(extreme_points)
Px = int(abs(mean(x for x, y in extreme_points) * 10_000))
Py = int(abs(mean(y for x, y in extreme_points) * 10_000))

print(Px, Py)

# tracer(0)
# screensize(5000, 5000)
# rt(90)
# r = 25
# up()
# for kl in clusters:
#     color = random(), random(), random()
#     for x, y in kl:
#         goto(x * r, y * r)
#         dot(3, color)
# for points in extreme_points:
#     color = 'red'
#     up()
#     for point in points:
#         x, y = point
#         goto(x * r, y * r)
#         down()
# update()
# done()
