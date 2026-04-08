from re import *

with open('01-k7.txt') as file:
    s = file.readline()

reg = r'C+'
# m = max(findall(reg,s), key=len)
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m), m)