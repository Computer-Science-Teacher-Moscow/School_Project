sm = 0
with open('3_3_1.txt') as file:
    for i, s in enumerate(file, 1):
        l = [int(x) for x in s.split()]
        if all(l[i] < l[i + 1] for i in range(len(l) - 1)) or len(set(l)) < 5:
            sm += i
            print(*l)
print(sm)
