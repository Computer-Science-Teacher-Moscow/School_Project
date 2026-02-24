from string import printable

for x in printable[:15]:
    for y in printable[:17]:
        expr = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if expr % 131 == 0:
            print(y, expr // 131)

