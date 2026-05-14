def f(x, y):
    return (x*y > A) or (x > y) or (800 >= x)


for A in range(643000,0,-1):
    if all(f(x, y) for x in range(790,810) for y in range(798, 805)):
        print(A)
        break
