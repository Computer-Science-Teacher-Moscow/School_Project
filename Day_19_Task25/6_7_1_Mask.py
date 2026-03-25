from fnmatch import fnmatch

mask = '1*23??56'

for n in range(171, 10 ** 8, 171):
    if fnmatch(str(n), mask):
        print(n, n // 171)
