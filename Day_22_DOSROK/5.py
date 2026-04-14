def get_r(n):
    r = bin(n)[2:]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    return int(r, 2)

for num in range(1, 1000):
    if get_r(num) > 253:
        print(num)
        break