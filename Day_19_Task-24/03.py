# метод 1 (линейный)

# with open('03_k7a-4.txt') as file:
#     s = file.readline()
# print(len(s))
# s = s.replace('D', ' ').split()
# print(m:=(max(s, key = len)), len(m))

# # метод 2 (2 цикла)
with open('03_k7a-4.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if 'D' not in c:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)
#
# # метод 3 (Регулярные выражения)

from re import *

with open('03_k7a-4.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'[^D]+'
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m), m)
