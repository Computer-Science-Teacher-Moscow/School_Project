res = []
for x in range(2030, 0, -1):
    cnt = 0
    n = 6 ** 2030 + 6 ** 100 - x
    while n:
        n, r = divmod(n, 6)
        if r == 0:
            cnt += 1
    res.append(cnt)
print(max(res))
