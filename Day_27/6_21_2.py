# with open('6_21_2.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# l = r = cnt_2025 = cnt_W = 0
# m = 10 ** 10
# for r in range(ls):
#     if s[r] == 'W': cnt_W += 1
#     if r > 2 and s[r - 3] + s[r - 2] + s[r - 1] + s[r] == '2025': cnt_2025 += 1
#     while cnt_W >= 90:
#         if s[l] == 'W': cnt_W -= 1
#         if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == '2025': cnt_2025 -= 1
#         l += 1
#         if cnt_2025 >= 110 and cnt_W == 90:
#             m = min(m, r - l + 1)
# print(m)

with open('6_21_2.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 10000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if c.count('2025') < 110:
            break
        if (cc:=c.count('W')) < 90:
            break
        if cc == 90:
            m = min(m, len(c))

print(m)
