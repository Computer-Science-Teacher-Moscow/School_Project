from itertools import product

word  = ''.join(sorted('ТЕОРИЯ'))
last_i = 0
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if i % 2 and w[0] not in 'РТЯ' and w.count('И') >= 2:
        last_i = i
print(last_i)