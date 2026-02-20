from itertools import product

word  = ''.join(sorted('АВОРТ'))


for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if w == 'ВОРОТА':
        print(i)
        break