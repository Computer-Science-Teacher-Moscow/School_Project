from itertools import product

cnt = 0
for pr in product('012345678', repeat=5):
    w = ''.join(pr)
    if w[0] != '0' and w.count('0') == 1 and all(x + '0' not in w and '0' + x not in w for x in '1357'):
        cnt += 1
        print(w)
print('---' * 3)
print(cnt)
