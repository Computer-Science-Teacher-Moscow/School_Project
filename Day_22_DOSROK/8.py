from itertools import product

word = ''.join(sorted('АПРЕЛЬ'))
print(word)

l = 0
for i, pr in enumerate(product(word, repeat = 5), 1):
    w = ''.join(pr)
    if i % 2 == 0 and w[0] not in 'ЬР' and w.count('Л') >=2:
        l = i
        print(i, w)
print(l)