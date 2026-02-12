def DEL(n, m):
    return n % m == 0

def f(x):
    return (not DEL(x,A)) <= ((not DEL(x,21)) and (not DEL(x,35)))

for A in range(1000, 0, -1):
    if all(f(x) for x in range(1, 10000)):
        print(A)
        break

