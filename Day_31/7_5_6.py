def f(x, y):
    return (68160 != 2 * y + 4 * x) or (x * y > A) or (x > y)


pairs = [(x, (68160 - 4 * x) // 2) for x in range(1, 17044) if
         68160 - 4 * x > 0 and (68160 - 4 * x) % 2 == 0]
print(len(pairs))

for A in range(34100, 0, -1):
    if all(f(x, y) for x, y in pairs):
        print(A)
        break
