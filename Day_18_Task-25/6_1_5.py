def get_divisors(n: int):
    divisors = set()
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors

cnt = 0
for num in range(500001, 10**10):
    divs = sorted(get_divisors(num))
    divs = [x for x in divs if x != 8 and x%10 == 8]
    if divs:
        print(num, min(divs))
        cnt +=1
    if cnt == 5:
        break