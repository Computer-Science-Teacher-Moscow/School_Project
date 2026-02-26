from itertools import product

word  = ''.join(sorted('ТАРКИ'))

for length in range(4, 10):
    for i, pr in enumerate(product(word, repeat=length), 1):
        w = ''.join(pr)
        for char in 'ТАРКИ':
            if char in 'АИ':
                w = w.replace(char, 'G')
            else:
                w = w.replace(char, 'S')
        if i % 2 == 0 and w[0] == 'S' and w.count('G') == 3 and 'GGG' in w:
            if i == 31314:
                print(length)
                exit()
            else:
                break
# Ответ: 7

