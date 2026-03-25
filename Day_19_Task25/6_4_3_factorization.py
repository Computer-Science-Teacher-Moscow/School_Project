def fact(n: int, p=2):
    for d in range(p, int(n ** 0.5) + 1):
        if n % d == 0:
            return [d] + fact(n // d, d)
    return [n]


cnt = 0
for num in range(5400001, 10 ** 10):
    prime_divs = fact(num)
    if len(prime_divs) > 1:
        m = min(prime_divs) + max(prime_divs)
        if m > 60000 and str(m) == str(m)[::-1]:
            print(num, m)
            cnt += 1
    if cnt == 5:
        break

print('-----')