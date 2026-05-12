with open('13_1.txt') as file:
    a = [int(x) for x in file]
# print(a)
N = min(x for x in a if abs(x) % 15 != 0)
res = []
for f, b, c in zip(a, a[1:], a[2:]):
    if all(x % N != 0 for x in tr):
        res.append(f+b+c)
print(len(res), max(res))
