from itertools import product

word  = ''.join(sorted('ПОЛЕНИЦА'))

for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if i % 2 != 0 and w[0] != 'А' and w[-1] != 'А' and w.count('Л') >= 3:
        print(i)
        break
