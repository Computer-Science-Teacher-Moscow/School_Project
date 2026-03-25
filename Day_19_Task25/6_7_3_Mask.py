from fnmatch import fnmatch
from math import prod

mask = '34*56?7'

for n in range(4321, 10 ** 9, 4321):
    if fnmatch(str(n), mask) and (pr:=prod(map(int, list(str(n))))) % 10 == 0:
        print(n, pr)
