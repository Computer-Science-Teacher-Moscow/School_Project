from math import dist
from statistics import mean

clustersA = ([], [])
clustersB = ([], [], [])

with open('6_10_1_27A.txt', 'r') as file:
    for point in file:
        x, y = map(float, point.split())
        if x < 1:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA))

with open('6_10_1_27B.txt', 'r') as file:
    for point in file:
        x, y = map(float, point.split())
        if y < 3:
            clustersB[0].append((x, y))
        elif y > 7:
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

centoidsA = [get_centroid(kl) for kl in clustersA]
centoidsB = [get_centroid(kl) for kl in clustersB]
# print(centoidsA)
# print(centoidsB)
PxA = int(mean(x for x, y in centoidsA) * 10_000)
PyA = int(mean(y for x, y in centoidsA) * 10_000)
PxB = int(mean(x for x, y in centoidsB) * 10_000)
PyB = int(mean(y for x, y in centoidsB) * 10_000)
print(PxA, PyA)
print(PxB, PyB)



