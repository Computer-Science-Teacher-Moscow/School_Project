from itertools import permutations

cnt=0
for pr in permutations('ABBBBE'):
    w = ''.join(pr)
    if 'BBBB' in w:
        cnt +=1
        print(w)
print('----' * 5)
print(cnt)