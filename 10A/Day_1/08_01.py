from itertools import product

word = ''.join(sorted('ВЕСНА'))

print(word)

for i, pr in enumerate(product(word, repeat=4), 1):
    w = ''.join(pr)
    if 'Е' not in w and 'АА' not in w:
        print(i, w)
        break