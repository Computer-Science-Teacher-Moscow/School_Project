from itertools import product

word  = ''.join(sorted('КЛРТ'))
# print(word)

for i, pr in enumerate(product(word, repeat=4), 1):
    if i == 67:
        print(*pr, sep='')
        break