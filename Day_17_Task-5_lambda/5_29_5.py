from string import printable as alf

def num_to_cs(n, cs):
    res = []
    while n:
        n, r = divmod(n, cs)
        res.append(alf[r])
    return ''.join(res)[::-1]

def get_r(n: int):
    r = num_to_cs(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += num_to_cs(n % 3 * 5, 3)
    return int(r, 3)

res = []
for num in range(1, 1000):
    R = get_r(num)
    if R > 133:
        res.append(R)
        print(R)
print(min(res))
