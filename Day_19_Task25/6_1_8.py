def get_divisors(n: int):
    divisors = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors


cnt = 0
for num in range(500001, 10 ** 10):
    r = sum(get_divisors(num))
    if r % 10 == 6:
        print(num, r)
        cnt += 1
    if cnt == 5:
        break
