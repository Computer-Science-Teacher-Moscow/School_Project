# # метод 2 (2 цикла)
with open('05_24-280.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if len(c) == len(set(c)):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)

