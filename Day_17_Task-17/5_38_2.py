with open('5_38_2_17-282.txt') as file:
    a = [int(x) for x in file]

res = []
min_el_k17 = min(x for x in a if x % 17 == 0)
# min_el_k17 = min(filter(lambda x: x % 17 == 0, a))
print(min_el_k17)

for pr in zip(a, a[1:]):
    if any(x % min_el_k17 == 0 for x in pr):
        res.append(sum(pr))
print(len(res), max(res))
