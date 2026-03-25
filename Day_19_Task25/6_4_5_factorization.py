def fact(n: int, p=2):
    for d in range(p, int(n ** 0.5) + 1):
        if n % d == 0:
            return [d] + fact(n // d, d)
    return [n]


cnt = 0
for num in range(89428305, 10 ** 12):
    if len(prime_divs := fact(num)) >= 6 and num % (sm := sum(prime_divs)) == 0:
        print(num, sm)
        cnt += 1
    if cnt == 6:
        break
