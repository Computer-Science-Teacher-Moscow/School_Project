def num_to_cs(n, cs):
    res = []
    while n:
        n, r = divmod(n, cs)
        res.append(str(r))
    return ''.join(res)[::-1]

def get_r(n: int):
    r = num_to_cs(n, 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += num_to_cs(n % 3 * 4, 3)
    return int(r, 3)

for num in range(1000,0, -1):
    R = get_r(num)
    if R < 199:
        print(num)
        break

