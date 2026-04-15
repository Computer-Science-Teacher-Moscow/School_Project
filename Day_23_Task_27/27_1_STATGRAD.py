from math import dist
from itertools import combinations

clustersA = ([], [])
clustersB = ([], [], [])

with open('27_A_STATGRAD.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        if x < 0:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA))

with open('27_B_STATGRAD.txt') as file:
    for s in file:
        x, y = map(float, s.split())
        if x < -14 or -1 < x < 1 or x > 9:
            pass
        elif y < -9:
            clustersB[0].append((x, y))
        elif 2 < x < 9:
            clustersB[1].append((x, y))
        else:
            clustersB[2].append((x, y))
print(*(len(kl) for kl in clustersB))


def get_intercluster_diameter(kl1, kl2):
    res = []
    for point in kl1:
        max_dist_kl = max((dist(point, p), (point, p)) for p in kl2)
        res.append(max_dist_kl)
    return max(res)


intercluster_diametersA = [get_intercluster_diameter(kl1, kl2) for kl1, kl2 in combinations(clustersA, 2)]
intercluster_diametersB = [get_intercluster_diameter(kl1, kl2) for kl1, kl2 in combinations(clustersB, 2)]
print(intercluster_diametersA)
print(intercluster_diametersB)

Px = int(abs(intercluster_diametersA[0][1][0][0]-intercluster_diametersA[0][1][1][0]) * 1000)
Px = int(abs(-13.784718943162 - 7.765008765718) * 1000)
Py = int((8.210938759434 - 6.264539572469) * 1000)

Q1 = int((29.323681245403442 + 23.596049510540418 + 18.489085699725322) * 100)
Q2 = int(max([dist(p, (1,1)) for d, points in intercluster_diametersB for p in points]) * 100)

print(Px, Py)
print(Q1, Q2)
