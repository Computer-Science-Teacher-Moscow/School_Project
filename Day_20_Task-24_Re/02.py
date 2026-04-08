from re import *

with open('02-k7a-1.txt') as file:
    s = file.readline()

# reg = r'[ABC]+'
reg = r'[^DE]+'
# m = max(findall(reg,s), key=len)
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m), m)