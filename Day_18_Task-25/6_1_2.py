def get_divisors(n: int):
    divisors = {1, n}
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors

res = []
for num in range(154026, 154044):
    divs = sorted(get_divisors(num))
    if len(divs) == 4:
        print(*divs[-2:])



