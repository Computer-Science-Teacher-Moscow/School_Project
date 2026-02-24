for x in range(2030, 0, -1):
    cnt = 0
    n = 3 ** 100 - x
    while n:
        n, r = divmod(n, 3)
        if r == 0:
            cnt += 1
    if cnt == 5:
        print(x)
        break
