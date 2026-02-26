from itertools import product

word  = ''.join(sorted('СДАЙЕГЭ'))

sm = 0
for i, pr in enumerate(product(word, repeat=6), 1):
    w = ''.join(pr)
    if 'ЕГЭ' in w:
        sm += i
        print(w)
print('---' * 5)
print(sm)

# Ответ: 79143659