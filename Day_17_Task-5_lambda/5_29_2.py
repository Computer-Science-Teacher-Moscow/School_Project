def get_r(n: int):
    r = f'{n:b}'
    # r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    return int(r, 2)

res = []
for num in range(1, 13):
    res.append(get_r(num))
print(max(res))
