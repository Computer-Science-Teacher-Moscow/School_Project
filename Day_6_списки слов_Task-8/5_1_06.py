from itertools import product

word  = ''.join(sorted('ЯНВАРЬ'))
last_i = 0
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if not w.startswith('Я') and w.count('Ь') <=1 and 'ЯЯ' not in w:
        last_i = i
print(last_i)