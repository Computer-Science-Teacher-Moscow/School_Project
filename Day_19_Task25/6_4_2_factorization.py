def fact(n: int, p=2):
    for d in range(p, int(n ** .5) + 1):
        if n % d == 0:
            return [d] + fact(n // d, d)
    return [n]


cnt = 0
for num in range(1_324_728, 10_000_000):
    if len(prime_divs := fact(num)) == 2 and all(str(x).count('5') == 1 for x in prime_divs):
        print(num, max(prime_divs))
        cnt += 1
    if cnt == 5:
        break