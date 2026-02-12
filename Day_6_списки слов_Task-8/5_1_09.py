from itertools import product

word  = ''.join(sorted('ПОРТ'))
cnt = 0
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if w in ('ТОПОР', 'РОПОТ'):
        print(i)
