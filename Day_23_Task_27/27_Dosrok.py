from math import dist
from itertools import combinations

clustersA = ([], [])
clustersB = ([], [], [])

with open('27_A_28766_DOSROK.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y, h = s.split()
        x, y = float(x), float(y)
        col = h[0]
        luminosity = h[1]
        size = h[2:]
        if y > 10:
            clustersA[0].append((x, y, col, luminosity, size))
        else:
            clustersA[1].append((x, y, col, luminosity, size))
clustersA = sorted(clustersA, key=len)
print(*(len(kl) for kl in clustersA))

with open('27_B_28766_DOSROK.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y, h = s.split()
        x, y = float(x), float(y)
        col = h[0]
        luminosity = h[1]
        size = h[2:]
        if x > 24:
            clustersB[0].append((x, y, col, luminosity, size))
        elif y > 24:
            clustersB[1].append((x, y, col, luminosity, size))
        else:
            clustersB[2].append((x, y, col, luminosity, size))
clustersB = sorted(clustersB, key=len)
print(*(len(kl) for kl in clustersB))


def get_centroids(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point[:2], p[:2]) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = [get_centroids(kl) for kl in clustersA]
centroidsB = [get_centroids(kl) for kl in clustersB]
print(centroidsA)
print(centroidsB)

A1 = int(min(dist(centroidsA[0][:2], p[:2]) for p in clustersA[0] if p[2] == 'Y' and p[-1] == 'III') * 10_000)
A2 = int(max(dist(centroidsA[0][:2], p[:2]) for p in clustersA[1] if p[2] == 'Y' and p[-1] == 'III') * 10_000)

yellow_supergiants = [[x for x in kl if x[2] == 'Z' and x[-1] == 'I'] for kl in clustersB]
print(*(len(kl) for kl in yellow_supergiants))
min_d_cl0 = min(dist(p1[:2], p2[:2]) for p1, p2 in combinations(yellow_supergiants[0], 2))
min_d_cl2 = min(dist(p1[:2], p2[:2]) for p1, p2 in combinations(yellow_supergiants[2], 2))
B1 = int(min((min_d_cl0, min_d_cl2)) * 10_000)
B2 = int(dist(centroidsB[1][:2], centroidsB[2][:2]) * 10_000)

print('-----')
print(A1, A2)
print(B1, B2)
