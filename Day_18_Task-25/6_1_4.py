def get_divisors(n: int):
    divisors = set()
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors

cnt = 0
for num in range(220_000, 10**10):
    divs = sorted(get_divisors(num))
    if divs:
        m = divs[0] + divs[-1]
        if m % 10 == 4:
            print(num, m)
            cnt+=1
    if cnt == 5:
        break




