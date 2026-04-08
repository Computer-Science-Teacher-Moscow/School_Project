from re import *

with open('09.txt') as file:
    s = file.readline()

num = r'([789][0789]*)'
expression = fr'{num}(\*{num})*'
expression = fr'{expression}(\-{expression})*'

# m = max(findall(num,s), key=len)

m = max((x.group() for x in finditer(expression, s)), key=len)
print(len(m), m)