from itertools import combinations
from math import prod

# a = 'ABCDE'
# for comb in combinations(a, 2):
#     print(*comb)

with open('17-10.txt') as file:
    a = [int(x) for x in file]

res = []
for pr in combinations(a, 2):
    if prod(pr) % 15 !=0 :
        res.append(sum(pr))
print(len(res), max(res))

