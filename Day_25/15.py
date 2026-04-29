def f(x, y):
    return (x * y < A) or (5 * x < y) or (486 <= x)

for A in range(1176000, 10**10):
    if all(f(x,y) for x in range(487) for y in range(485*5+2)):
        print(A)
        break