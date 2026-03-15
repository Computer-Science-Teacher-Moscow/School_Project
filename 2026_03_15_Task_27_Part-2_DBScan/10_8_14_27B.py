from math import dist
from turtle import *
from random import random
from itertools import combinations
from statistics import mean

clusters = []
data = []
with open('10_8_13-14_27B.txt') as file:
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
clusters.sort(key=len)
print(*(len(kl) for kl in clusters))
clusters = tuple(kl for kl in clusters if len(kl) > 15)
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


def get_Q1_points():
    res = []
    kl_a, kl_b = clusters[0], clusters[-1]
    print(len(kl_b), len(kl_b))
    res_1 = []
    for point in kl_a:
        min_dist = min((dist(point, p), (point, p)) for p in kl_b)
        res_1.append(min_dist)
    res.append(min(res_1)[1])
    return res

min_max_len = get_Q1_points()
print(min_max_len)

Q1 = int(dist(min_max_len[0][0], min_max_len[0][1]) * 10_000)
extreme_points_dist_to_00 = [dist(p, (0, 0)) for points in get_extreme_points() for p in points]
Q2 = int(max(extreme_points_dist_to_00) * 10000)
print(Q1, Q2)
