from fnmatch import fnmatch

mask = '12*567?'

for n in range(0, 10 ** 10, 15554):
    if fnmatch(str(n), mask) and n % 2 == 0:
        print(n, n // 7777)
