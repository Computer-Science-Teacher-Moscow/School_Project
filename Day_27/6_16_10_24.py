with open('6_16_10_24.txt') as file:
    s = file.readline()
print((ls := len(s)))

l = r = m = cnt_FSRQ = 0
for r in range(ls):
    if r > 2 and s[r - 3] + s[r - 2] + s[r - 1] + s[r] == 'FSRQ': cnt_FSRQ += 1
    while cnt_FSRQ > 80:
        if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == 'FSRQ': cnt_FSRQ -= 1
        l += 1
    if cnt_FSRQ == 80:
        m = max((m, r - l + 1))
    r += 1
print(m)

# with open('6_16_10.txt') as file:
#     s = file.readline()
# ls = len(s)

# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if (cc := c.count('FSRQ')) <= 80:
#             if cc == 80:
#                 m = max(m, len(c))
#         else:
#             break
# print(m)
