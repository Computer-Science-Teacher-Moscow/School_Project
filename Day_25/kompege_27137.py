# Задача с kompege #27137

pairs1 = [(x, (1241651 - 5 * x)) for x in range(1, 248335)]
pairs1 = set([(x, y) for x, y in pairs1 if y >= 0])
# print(len(pairs1))
pairs2 = [(x, (413184 - x) / 2) for x in range(1, 413184)]
pairs2 = [(x, y) for x, y in pairs2 if y > 0 and y.is_integer()]

c = pairs1.union(pairs2)


def f(x, y):
    return (1241651 != 5 * x + y) and (413184 != x + 2 * y)or (A>x) or (A>y)

for A in range(1241651):
    if all(f(x,y) for x, y in c):
        print(A)
        break
