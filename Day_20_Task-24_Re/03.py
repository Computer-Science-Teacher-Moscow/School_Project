from re import *

with open('03.txt') as file:
    s = file.readline()

reg = r'(BA|CA|DA|BO|CO|DO)+'

# m = max(findall(reg,s), key=len)
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m) // 2, m)