for p in range(8, 37):
    expr = int(f'11353712', p) + int(f'135421', p)
    if expr % 31 == 0:
        print(expr // 31, p)
        break
