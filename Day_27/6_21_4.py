with open('6_21_4.txt') as file:
    s = file.readline()
print((ls := len(s)))

l = r = cnt_Z = 0
m = 10 ** 6
for r in range(ls):
    if s[r] == 'Z': cnt_Z += 1
    while cnt_Z >= 270:
        if s[l] == 'Z': cnt_Z -= 1
        l += 1
        if cnt_Z >= 270:
            m = min(m, r - l + 1)
print(m)


