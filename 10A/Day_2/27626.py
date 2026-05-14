n = 6 ** 2030 + 6 ** 100
res = []
for x in range(1, 2031):
    cnt_0 = 0
    n1 = n - x
    while n1 != 0:
        n1, r = divmod(n1, 6)
        if r == 0:
            cnt_0 += 1
    res.append(cnt_0)
print(min(res))
