from itertools import product

word  = ''.join(sorted('АЛГОРИТМ'))
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if i % 2 == 0 and w[0] not in 'АГ' and w.count('Р') >= 2:
        print(i)
        break