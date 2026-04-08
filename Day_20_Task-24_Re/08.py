# from re import *
#
# with open('08.txt') as file:
#     s = file.readline()
#
# num = r'([1-9][0-9]*|0)'
# expression = fr'({num}\*)*0(\*{num})*'
# expression = fr'{expression}(\+{expression})*'
#
# # m = max(findall(num,s), key=len)
# m = max((x.group() for x in finditer(expression, s)), key=len)
# print(len(m), m)

from re import *

with open('08.txt') as file:
    s = file.readline()

num = r'([1-9][0-9]*|0)'
expression = fr'{num}(\*{num})*'
expression = fr'{expression}(\+{expression})*'

# m = max(findall(num,s), key=len)
m = [x.group() for x in finditer(expression, s)]
m = max(m, key=eval)
print(eval(m))
# print(len(m), eval(m), m)