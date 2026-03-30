from itertools import product

comb = []
for l in 0, 1, 2, 3:
    for x in product('0123456789', repeat=l):
        comb.append(''.join(x))
print(comb)

res = []
for a1 in '0123456789':
    for a2 in comb:
        if (x := int(f'123{a1}4{a2}5679')) % 4013 == 0:
            res.append((x, x // 4013))
res.sort()
for r in res:
    print(*r)
