from itertools import product

word  = ''.join(sorted('КОМПЬЮТЕР'))
last_i = 0
for i, pr in enumerate(product(word, repeat=5), 1):
    w = ''.join(pr)
    if i % 2 != 0 and not w.startswith('Ь') and w.count('К') == 2:
        last_i = i
print(last_i)