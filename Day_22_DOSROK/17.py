with open('17_28762.txt') as file:
    a = [int(x) for x in file]
min_el_l23 = min(x for x in a if x % 23 == 0)
print(min_el_l23)

res = []
for pr in zip(a, a[1:]):
    if any(x % min_el_l23 == 0 for x in pr):
        res.append(sum(pr))
        # print(*pr)
print(len(res), max(res))
