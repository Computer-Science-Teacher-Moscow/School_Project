def get_divisors(n: int):
    divisors = {1, n}
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return sorted(divisors)

for num in range(164700, 164753):
    divs = get_divisors(num)
    if len(divs) == 6:
        print(*divs[-2:])
