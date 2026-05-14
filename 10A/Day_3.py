for x in '0123456789AB':
    expression = int(f'154{x}3', 12) + int(f'1{x}365', 12)
    if expression % 13 == 0:
        print(expression//13)
        break