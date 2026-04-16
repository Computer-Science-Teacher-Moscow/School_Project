from math import dist
from statistics import mean
from itertools import combinations

clustersA = ([], [])
clustersB = ([], [], [])

with open('12_2_27A.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if x > 6 or 0 < y < 4 or (x < -6 and y > 6):
            pass
        elif y < 0:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA))

with open('12_2_27B.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if x < -15 or x > 9 or y < -15 or y > 7:
            pass
        elif x < -6:
            clustersB[0].append((x, y))
        elif x > -3 and y < -5:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
print(*(len(kl) for kl in clustersB))


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point, p) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = [get_centroid(kl) for kl in clustersA]
centroidsB = [get_centroid(kl) for kl in clustersB]

Px = int(abs(mean(x for x, y in centroidsA) * 10_000))
Py = int(abs(mean(y for x, y in centroidsA) * 10_000))

print(Px, Py)

Q1 = int(min(dist(p1,p2) for p1, p2 in combinations(centroidsB,2)) * 10000)
Q2 = int(max(dist(p1,p2) for p1, p2 in combinations(centroidsB,2)) * 10000)

print(Q1, Q2)