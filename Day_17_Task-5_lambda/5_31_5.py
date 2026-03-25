def num_to_cs(n, cs):
    res = []
    if n == 0:
        res.append('0')
    while n:
        n, r = divmod(n, cs)
        res.append(str(r))
    return ''.join(res[::-1])


def get_r(n: int):
    r = num_to_cs(n, 5)
    if not num % 2:
        r += num_to_cs(int(r[-1]) * 3, 5)
    else:
        r = r[-1] + r[1:-1] + r[0] + '1'
    r = r.lstrip('0')
    return r

for num in range(1, 100000):
    if get_r(num).count('0') == 4:
        print(num)
        break

print(get_r(250))
