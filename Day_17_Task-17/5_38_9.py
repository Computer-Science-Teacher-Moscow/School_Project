with open('5_38_9.txt') as file:
    a = [int(x) for x in file]

res = []
min_el_3z_end15 = min(x for x in a if 99 < abs(x) < 1000 and abs(x) % 100 == 15)
print(min_el_3z_end15)

for tr in zip(a, a[1:], a[2:]):
    if (all(x < 0 for x in tr) or all(x > 0 for x in tr) or all(x == 0 for x in tr)) and (p:=max(tr) * min(tr)) > min_el_3z_end15 ** 2:
        res.append(p)
        print(*tr)
print(len(res), min(res))
