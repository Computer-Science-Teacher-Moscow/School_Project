def f(x):
    Q = 29 <= x <= 47
    return ((not x % 3 == 0) and (x not in {48, 52, 56})) <= (((abs(x - 50) <= 7) <= Q) or (x & A == 0))


for A in range(1, 1000):
    if all(f(x) for x in range(-10000, 10000)):
        print(A)
        break
