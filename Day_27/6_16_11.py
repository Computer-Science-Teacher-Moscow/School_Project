with open('6_16_11_24.txt') as file:
    s = file.readline()
print((ls := len(s)))

l = r = m = cnt_SG = 0
for r in range(ls):
    if r > 0 and s[r - 1] + s[r] in ('BA', 'CA', 'DA', 'BO', 'CO', 'DO')
