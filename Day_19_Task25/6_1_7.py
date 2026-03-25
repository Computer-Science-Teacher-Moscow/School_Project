def get_divisors(n: int):
    divisors = set()
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors


cnt = 0
for num in range(424_243, 10 ** 10):
    divs = get_divisors(num)
    if divs and (m := sum((min(divs), max(divs)))) % 2024 == 42:
        print(num, m)
        cnt += 1
    if cnt == 8:
        break
