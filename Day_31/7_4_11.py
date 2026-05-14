def f(x, y):
    return (y < A) and (x < 5*A) or (143753 < 23*y + 3*x)


for A in range(9580, 10000):
    if all(f(x, y) for x in range(47890, 47950) for y in range(1, 3)):
        print(A)
        break