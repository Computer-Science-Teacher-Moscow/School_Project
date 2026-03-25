def get_divisors(n: int):
    divisors = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divisors.add(d)
            divisors.add(n // d)
    return divisors


cnt = 0
for num in range(5700000 - 1, 0, -1):
    res = []
    if '2' in str(num):
        divs = get_divisors(num)
        divs_odd_k131 = [x for x in divs if x % 2 != 0 and x % 131 == 0]
        divs_even_wo3 = [x for x in divs if x % 2 == 0 and '3' not in str(x)]
        for x in divs_even_wo3:
            for y in divs_odd_k131:
                pr = (x, y)
                if x * y == num:
                    res.append((num, max(pr), y))
        if res:
            print(*min(res, key = lambda x: x[-1])[:-1])
            cnt+=1
    if cnt == 5:
        break
