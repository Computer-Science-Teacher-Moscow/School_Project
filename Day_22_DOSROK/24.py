# метод двух циклов

# with open('24_28765.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if c.count('BC') <= 180:
#             m = max(m, len(c))
#             print(c)
#         else:
#             break
# print(m)

# метод двух указателей
with open('24_28765.txt') as file:
    s = file.readline()
print((ls := len(s)))

l, m, cnt_BC = 0, 0, 0
for r in range(ls):
    if s[r - 1] + s[r] == 'BC': cnt_BC += 1
    while cnt_BC > 180:
        if s[l] + s[l + 1] == 'BC': cnt_BC -= 1
        l += 1
    if cnt_BC <= 180: m = max(m, r - l + 1)
print(m)
