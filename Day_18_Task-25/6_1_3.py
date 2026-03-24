def get_divisors(n: int):
    divisors = {1, }
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors

res = []
for num in range(397438, 443521):
    divs = sorted(x for x in get_divisors(num) if x % 2 == 0)
    if len(divs) >= 142:
        print(len(divs), max(divs))



