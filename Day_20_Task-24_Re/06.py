from re import *

with open('06.txt') as file:
    s = file.readline()

num = r'([1-9A-F][0-9A-F]*|0)'
reg = fr'(?=({num}))'

# m = max(findall(num,s), key=len)
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)