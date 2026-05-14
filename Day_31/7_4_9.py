def f(x, y):
    return (3678744 != 11 * y + 13 * x) or (A < x) or (A < y)


for A in range(153500, 0, -1):
    if all(f(x, y) for x in range(153000, 153500) for y in range(153000, 153500)):
        print(A)
        break
