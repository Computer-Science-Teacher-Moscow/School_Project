sm = 19**270 + 19**240 + 19**190 + 19**180
for x in range(1, 1000):
    cnt = 0
    m = sm - x
    while m:
        m, r = divmod(m, 19)
        if r == 18: cnt += 1
    if cnt == 177:
        print(x)
        break