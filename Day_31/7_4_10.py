def f(x, y):
    return (y < 7 * A) and (x < 3 * A) or (21135281 < 11 * y + 13 * x)


for A in range(541000, 1000000):
    if all(f(x, y) for x in range(1625000, 1627000) for y in range(1, 3)):
        print(A)
        break