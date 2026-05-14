from string import printable as a


for x in a[:23]:
    expression = int(f'761{x}035', 23) + int(f'338{x}932', 23)
    if expression % 22 == 0:
        print(expression//22)
        break