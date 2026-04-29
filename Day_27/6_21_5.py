from string import ascii_uppercase as alf

with open('6_21_5.txt') as file:
    s = file.readline()
print((ls := len(s)))

alf = set(alf)
m = 1000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if set(c) == alf:
            m = min(m, len(c))
print(m)
