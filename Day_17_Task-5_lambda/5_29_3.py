def get_r(n: int):
    r = f'{n:b}'
    for _ in range(2):
        r += str(r.count('1') % 2)
    return int(r, 2)

res = []
for num in range(1, 1000):
    R = get_r(num)
    if R > 75:
        res.append(R)
print(min(res))
