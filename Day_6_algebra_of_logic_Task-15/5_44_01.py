def f(x):
    return (not x % A == 0) <= ((x % 6 == 0) <= (not x% 4==0))

for A in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(A)

# def f():
#     A = 1
#     print('Local id A', id(A))
#
# A = 2
# print('Global id A', id(A))
# f()
print('Global id A', id(A))