from fnmatch import fnmatch


def get_divisors(n: int):
    divisors = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors


mask = '2*3?'

cnt = 0
for n in range(500000, 10 ** 9):
    divs = get_divisors(n)
    divs = [x for x in divs if fnmatch(str(x), mask)]
    if divs:
        print(n, min(divs))
        cnt += 1
    if cnt == 5:
        break
