from re import *

with open('6_21_9.txt') as file:
    s = file.readline()
print(((ls := len(s))))

num = r'[1-9ABCDE][0-9ABCDE]*[05]'
reg = fr'(?=({num}))'
m = [x.group(1) for x in finditer(reg, s)]
# m = [x for x in m if int(x, 15) % 5 == 0]
m = max(m, key=lambda x: int(x, 15))
# m = max(m, key=int_12)
print(m, sep='\n')
start = s.index(m)
end = start + len(m)
print(s[start:end])
print(end - 1)
