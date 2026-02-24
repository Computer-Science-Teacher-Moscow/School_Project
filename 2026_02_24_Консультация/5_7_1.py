n = 27 ** 4 - 9 ** 5 + 3 ** 8 - 25
cnt = 0
while n:
    n, r  = divmod(n, 3)
    if r  == 2:
        cnt += 1
print(cnt)

