from math import dist
from statistics import mean
from turtle import *
from random import random

clastersB = ([], [], [])

with open('07_27B.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if y < -x + 8:
            clastersB[0].append((x, y))
        elif y > 1.4 * x - 5.5:
            clastersB[1].append((x, y))
        else:
            clastersB[2].append((x, y))
print(*(len(kl) for kl in clastersB))

# tracer(0)
# r = 30
# screensize(5000, 5000)
# up()
# for kl in clastersB:
#     color = random(), random(), random()
#     for p in kl:
#         x, y = p
#         goto(x * r, y * r)
#         dot(3, color)
# update()
# done()

def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point, p) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1]


# centroidsA = [get_centroid(kl) for kl in clastersA]
centroidsB = [get_centroid(kl) for kl in clastersB]

# PxA = int(mean(x for x, y in centroidsA) * 100_000)
# PyA = int(mean(y for x, y in centroidsA) * 100_000)

PxB = int(mean(x for x, y in centroidsB) * 100_000)
PyB = int(mean(y for x, y in centroidsB) * 100_000)

# print(PxA, PyA)
print(PxB, PyB)
