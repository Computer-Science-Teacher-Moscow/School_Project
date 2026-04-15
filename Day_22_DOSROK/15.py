def f(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2
    return P <= ((Q and not A) <= (not P))


ox = [dx for x in (25, 64, 40, 115) for dx in (x - 0.001, x, x + 0.001)]
res = []
for a1 in ox:
    for a2 in ox:
        if a1 <= a2 and all(f(x) for x in range(-10000, 10000)):
            res.append(a2 - a1)
print(min(res))
