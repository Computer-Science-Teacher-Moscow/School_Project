from string import printable as alf

alf = alf[:15]
for x in alf:
    expr = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if expr % 14 == 0:
        print(expr // 14)
        break
