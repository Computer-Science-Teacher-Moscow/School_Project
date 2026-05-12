from cgi import print_environ_usage
from itertools import product

word = ''.join(sorted('СИМВОЛ'))
print(word)

last_n = 0
for i, pr in enumerate(product(word, repeat = 5), 1):
    w = ''.join(pr)
    if i % 2 != 0 and w[0] not in 'ОС' and w.count('В') == 1 and w.count('С') <= 1:
        print(i, w)
        last_n = i
print('----' * 3)
print(last_n)
