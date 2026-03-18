with open('5_38_3_17-381.txt') as file:
    a = [int(x) for x in file]

res = []
max_el_4z_end39 = max(x for x in a if 999 < abs(x) < 10_000 and abs(x) % 100 == 39)
print(max_el_4z_end39)

for pr in zip(a, a[1:]):
    if sum(999 < abs(x) < 10_000 for x in pr) == 1 and sum(pr) ** 2 <= max_el_4z_end39 ** 2:
        res.append(sum(pr))
print(len(res), max(res))

