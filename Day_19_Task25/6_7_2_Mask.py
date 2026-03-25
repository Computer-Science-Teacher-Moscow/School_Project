from fnmatch import fnmatch

mask = '3?12?14*5'

for n in range(1917, 10 ** 10, 1917):
    if fnmatch(str(n), mask):
        print(n, n // 1917)
