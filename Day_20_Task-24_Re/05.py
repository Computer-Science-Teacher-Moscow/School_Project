from re import *

with open('05.txt') as file:
    s = file.readline()

reg = r'(LMN|MN|N){,1}(KLMN)+(KLM|KL|K){,1}'
reg = fr'(?=({reg}))'

# m = max(findall(reg,s), key=len)
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)