def get_r(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    return int(r, 2)

for num in range(1, 100):
    R = get_r(num)
    if 52< R < 60:
        print(R)

