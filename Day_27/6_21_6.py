with open('6_21_6.txt') as file:
    s = file.readline()
print(((ls := len(s))))

l = r = cnt_E = 0
m = 100000
for r in range(ls):
    if s[r] == 'E': cnt_E += 1
    while cnt_E >= 100:
        if s[l] == 'E': cnt_E -= 1
        l += 1
        if cnt_E == 100:
            m = min(m, r - l + 1)
print(m)
