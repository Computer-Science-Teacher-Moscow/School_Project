with open('5_38_7.txt') as file:
    a = [int(x) for x in file]

res = []
max_el_end30 = max(x for x in a if abs(x) % 100 == 30)
print(max_el_end30)

for tr in zip(a, a[1:], a[2:]):
    if sum(999 < abs(x) < 10_000 for x in tr) == 0 and (sm:=sum(tr)) > max_el_end30:
        res.append(sm)
print(len(res), max(res))

