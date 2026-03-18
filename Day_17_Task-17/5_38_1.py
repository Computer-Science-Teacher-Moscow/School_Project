with open('5_38_1_17-404.txt') as file:
    a = [int(x) for x in file]

res = []
min_el = min(a)
for pr in zip(a, a[1:]):
    if any(x % 55 == min_el for x in pr):
        res.append(sum(pr))
print(len(res), min(res))
