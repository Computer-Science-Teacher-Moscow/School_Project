def get_divisors(n: int):
    divisors = {n}
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors


def ОД(n, m):
    # print(get_divisors(n),get_divisors(m), sep='\n')
    return bool(get_divisors(n) & get_divisors(m))


def f(x):
    return (ОД(x, 42) <= (not ОД(x, 7))) or (x + A >= 25)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break
