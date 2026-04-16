from string import ascii_uppercase as alf


alf = set(alf)

with open('12_2_24-371.txt') as file:
    s = file.readline().split('.')

s = [x.lstrip() + '.' for x in s if alf.difference(x) == set() and x[-1] in alf]
m = min(s, key=len)

print(len(m), m,'|',sorted(set(m)))



