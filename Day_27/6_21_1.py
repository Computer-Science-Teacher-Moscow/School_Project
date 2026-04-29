with open('6_21_1.txt') as file:
    s = file.readline()
print((ls := len(s)))

l = r = cnt_dot = 0
m = 10 ** 10
for r in range(ls):
    if s[r] == '.': cnt_dot += 1
    while cnt_dot >= 7:
        if s[l] == '.': cnt_dot -= 1
        m = min(m, r - l + 1)
        l += 1

print(m)

with open('6_21_1.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 10000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if (cc:=c.count('.')) <= 7:
            if cc == 7:
                m = min(m, len(c))
print(m)