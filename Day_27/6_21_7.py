with open('6_21_7.txt') as file:
    s = file.readline()
print(((ls := len(s))))
for char in '02468':
    s = s.replace(char, ' ')
s = s.split()
s = [x for x in s if len(set(x)) == 1 and x[0] not in '1234567890']
m = max(s, key=len)
print(len(m) + 2)
