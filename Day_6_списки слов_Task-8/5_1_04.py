word = 'АЁРТШ'

from itertools import product

w = ''.join('АЁРТШ')
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if w.count('А') <= 1 and 'ЁЁ' not in w:
        print(i)
        break