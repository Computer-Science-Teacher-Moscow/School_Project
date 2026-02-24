from string import printable

for x in printable[:11]:
    expr = int(f'3364{x}', 11) + int(f'{x}7946', 12) == int(f'55{x}87', 14)
    if expr:
        print(int(f'55{x}87', 14))
        break
