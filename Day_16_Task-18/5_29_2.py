def get_r(n):
    r = f'{n:b}'
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    return int(r, 2)

res = []
for num in range(1, 13):
    R = get_r(num)
    res.append(R)
print(max(res))
