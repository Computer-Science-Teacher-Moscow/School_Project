from string import ascii_uppercase, digits

with open('24.txt') as file:
    s = file.readline()
print((ls := len(s)))

for char in digits:
    s = s.replace(char, ' ')
s = s.split()
alf = set(ascii_uppercase)
s = [x for x in s if alf == set(x)]
m = max(s, key=len)
print(len(m), m)