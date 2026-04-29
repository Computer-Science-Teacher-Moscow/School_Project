from re import *

# def int_12(s: str):
#     return int(s, 12)


with open('6_21_8.txt') as file:
    s = file.readline()
print(((ls := len(s))))

num = r'[1-9AB][0-9AB]*'
reg = fr'(?=({num}))'
m = [x.group(1) for x in finditer(reg, s)]
m = [x for x in m if int(x, 12) % 6 == 0]
m = max(m, key=lambda x: int(x, 12))
# m = max(m, key=int_12)
print(m, sep='\n')
start = s.index(m)
end = start + len(m)
print(s[start:end])
print(end - 1)
