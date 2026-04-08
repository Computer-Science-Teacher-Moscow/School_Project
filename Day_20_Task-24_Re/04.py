from re import *

with open('04.txt') as file:
    s = file.readline()

reg = r'(NPO|PNO)+'
reg = fr'(?=({reg}))'

# m = max(findall(reg,s), key=len)
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)