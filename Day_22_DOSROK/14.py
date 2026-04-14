n = 2 * 2187 ** 567 + 729 ** 566 - 2 * 243 ** 565 + 81 ** 564 - 2 * 27 ** 563 - 6561
cnt = 0
while n:
    n, r = divmod(n, 27)
    if r > 9 and r % 2 == 0:
        cnt += 1
print(cnt)
