with open('5_38_6_17-409.txt') as file:
    a = [int(x) for x in file]

res = []
max_el_4z_end7 = max(x for x in a if 999 < abs(x) < 10_000 and abs(x) % 10 == 7)
print(max_el_4z_end7)

for tr in zip(a, a[1:], a[2:]):
    if sum(999 < abs(x) < 10_000 and abs(x) % 10 == 7 for x in tr) >= 2 and (sm:=sum(tr)) > max_el_4z_end7:
        res.append(sm)
print(len(res), max(res))

