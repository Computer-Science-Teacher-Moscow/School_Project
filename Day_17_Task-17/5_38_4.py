with open('5_38_4.txt') as file:
    a = [int(x) for x in file]

res = []
max_el_5z_end43 = max(x for x in a if 9999 < abs(x) < 100_000 and abs(x) % 100 == 43)
print(max_el_5z_end43)

for tr in zip(a, a[1:], a[2:]):
    if any(9999 < abs(x) < 100_000 and abs(x) % 100 == 43 for x in tr) and (sm:=sum(x ** 2 for x in tr)) <= max_el_5z_end43 ** 2:
        res.append(sm)
print(len(res), min(res))

