def get_r(n: int):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin(n % 3 * 3)[2:]
    return int(r, 2)

# print(get_r(12))
# print(get_r(4))


for num in range(1000, 0, -1):
    R = get_r(num)
    print(num, R)
    if R < 130:
        print('----' * 5)
        print(num)
        break
