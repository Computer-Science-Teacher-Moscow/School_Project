def get_r(n: int):
    r = f'{n:b}'
    if sum(int(x) for x in r) % 2 == 0:
        r += '0'
        r = '10' + r[2:]
    else:
        r += '1'
        r = '11' + r[2:]
    return int(r, 2)

for num in range(1, 1000):
    R = get_r(num)
    if R >= 16:
        print(num)
        break
