from fnmatch import fnmatch

mask = '1592*6?8'

for n in range(1996, 10 ** 10, 1996):
    n1 = str(n)[4:-3]
    if fnmatch(str(n), mask) and all(x in '02468' for x in n1):
        print(n, n // 1996)
