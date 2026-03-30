# # Метод двух циклов
#
with open('6_19_4_24-359.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 100000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if (cc := c.count('2025')) >= 90 and (ce:=c.count('E')) <= 110:
            if ce == 110  and cc  >= 90:
                m = min(m, len(c))
                print(m, c)
            else:
                break
print(m)