def num_to_cs(n, cs):
    res = []
    while n:
        n, r = divmod(n, cs)
        res.append(str(r))
    return ''.join(res)[::-1]


def get_r(n: int):
    r = num_to_cs(n, 3)
    if (sm:=sum(int(x) for x in r)) % 4 == 0:
        r = '1' + r[:-2]
    else:
        r += num_to_cs((sm % 4) * 3, 3)
    return int(r, 3)

res = []
for num in range(1, 10000):
    R = get_r(num)
    if 353 < R < 370:
        res.append(R)
print(min(res))