n = 9 ** 7 + 3 ** 21 - 8
sm = 0
while n:
    n, r = divmod(n, 3)
    sm += r
print(sm)
