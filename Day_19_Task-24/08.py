# # метод 2 (2 цикла)
# with open('08_k7a-6.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
# s = s.replace('A', '*').replace('E', '*').split('*')
# print(len(max(s,key=len)))


# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if 'A'  not in c and 'E' not in c:
#             m = max(m, len(c))
#             print(c)
#         else:
#             break
# print(m)

from re import *

with open('08_k7a-6.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'[^AE]+'
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m), m)
