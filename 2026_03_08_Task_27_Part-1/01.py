from math import dist
from statistics import mean

clastersA = ([], [])
clastersB = ([], [], [])

with open('01_27A.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        if x < 1:
            clastersA[0].append((x, y))
        else:
            clastersA[1].append((x, y))
print(*(len(kl) for kl in clastersA))

with open('01_27B.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        if y > 7:
            clastersB[0].append((x, y))
        elif y < 3:
            clastersB[1].append((x, y))
        else:
            clastersB[2].append((x, y))
print(*(len(kl) for kl in clastersB))


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point, p) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = [get_centroid(kl) for kl in clastersA]
centroidsB = [get_centroid(kl) for kl in clastersB]

PxA = int(mean(x for x, y in centroidsA) * 10_000)
PyA = int(mean(y for x, y in centroidsA) * 10_000)

PxB = int(mean(x for x, y in centroidsB) * 10_000)
PyB = int(mean(y for x, y in centroidsB) * 10_000)

print(PxA, PyA)
print(PxB, PyB)