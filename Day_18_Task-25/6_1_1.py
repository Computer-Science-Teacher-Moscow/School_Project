from math import prod

def get_divisors(n: int):
    divisors = set()
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors

res = []
for num in range(174457,174506):
    divs = list(get_divisors(num))
    if len(divs) == 2:
        res.append((prod(divs), sorted(divs)))
res.sort()
for p, divs in res:
    print(*divs)



