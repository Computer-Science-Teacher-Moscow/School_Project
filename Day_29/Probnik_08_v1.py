from itertools import product

cnt = 0
for w in product('0123456789ABCDEF', repeat=4):
    w = ''.join(w)
    if w[0] != '0' and w.count('D') == 1 and all(f'{x}D' not in w and f'D{x}' not in w for x in '13579BDF'):
        cnt += 1
print(cnt)
