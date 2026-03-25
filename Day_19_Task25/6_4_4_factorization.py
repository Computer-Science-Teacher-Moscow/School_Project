def fact(n: int, p=2):
    for d in range(p, int(n ** 0.5) + 1):
        if n % d == 0:
            return [d] + fact(n // d, d)
    return [n]


cnt = 0
for num in range(1474999, 0, -1):
    if (s := sum(set(fact(num)))) and s <= 42_000 and s % 6 == 0:
        print(num, s)
        cnt += 1
    if cnt == 5:
        break

print('-----')


def is_prime(n: int):
    return n > 1 and all(n % d != 0 for d in range(2, int(n ** .5) + 1))


def get_prime_divs(n: int):
    divs = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return [x for x in sorted(divs) if is_prime(x)]


cnt = 0
for n in range(1474999, 1, -1):
    if cnt == 5: break
    s = sum(get_prime_divs(n))
    if s != 0 and s <= 42000 and s % 6 == 0:
        print(n, s)
        cnt += 1
