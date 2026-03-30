# # Метод двух циклов
#
with open('6_19_4_02_22.txt') as file:
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

# Метод двух указателей

with open('6_19_4_02_22.txt') as file:
    s = file.readline()

l, m, cnt_2025, cnt_E = 0, 4000, 0, 0

for r in range(len(s)):
    if s[r] == 'E': cnt_E += 1
    if r > 2 and s[r - 3] + s[r - 2] + s[r - 1] + s[r] == '2025': cnt_2025 += 1
    while cnt_E >= 110 and cnt_2025 >= 90:
        if s[l] == 'E': cnt_E -= 1
        if l > 2 and s[l - 3] + s[l - 2] + s[l - 1] + s[l] == '2025': cnt_2025 -= 1
        l += 1
        if cnt_E == 110 and cnt_2025 >= 90:
            m = min(m, r - l + 1)
print(m)