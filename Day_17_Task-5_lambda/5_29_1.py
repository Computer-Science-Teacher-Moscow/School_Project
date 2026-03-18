def get_r(n:int):
    r = f'{n:b}'
    # r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    return int(r, 2)

res = []
for num in range(1, 1000):
    if (R:=get_r(num)) > 52:
        res.append(R)
print(min(res))