# метод 1 (линейный)
#
# with open('02_k7a-1.txt') as file:
#     s = file.readline()
# print(len(s))
# s = s.replace('D', ' ').replace('E', ' ').split()
# print(m:=(max(s, key = len)), len(m))

# метод 2 (2 цикла)
with open('02_k7a-1.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(x in 'ABC' for x in c):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)

# метод 3 (Регулярные выражения)

from re import *

with open('02_k7a-1.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'[ABC]+'
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m), m)



