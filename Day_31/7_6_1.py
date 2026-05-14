with open('7_6_1_24-378.txt') as file:
    s = file.readline()
print((ls := len(s)))
alf = 'ABCDEF'
digits = {str(x): 0 for x in range(10)}
print(digits)

l = r = cnt_alf = 0
m = 100000
for r in range(ls):
    if s[r] in alf: cnt_alf += 1
    if s[r].isdigit(): digits[s[r]] += 1
    while cnt_alf >= 3:
        if s[l] in alf: cnt_alf -= 1
        if s[l].isdigit(): digits[s[l]] -= 1
        l += 1
        if cnt_alf == 3 and all(x > 0 for x in digits.values()):
            m = min(m, r - l + 1)
print(m)
