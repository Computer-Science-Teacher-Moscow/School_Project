# №4
# def f(x):
#     P = 22 <= x <= 72
#     Q = 42 <= x <= 102
#     A = a1 <= x <= a2
#     return not((not A) and P) or Q
#
# ox = [dx for x in (22,72,42,102) for dx in (x - 0.0001, x, x + 0.0001)]
#
# res = []
# for a1 in ox:
#     for a2 in ox:
#         if a1<=a2 and all(f(x) for x in ox):
#             res.append(a2-a1)
# print(min(res))

# # №5
# def f(x):
#     P = 12 <= x <= 62
#     Q = 52 <= x <= 92
#     A = a1 <= x <= a2
#     return not ((not A) and P) or Q
#
#
# ox = [dx for x in (12, 62,52,92) for dx in (x - 0.0001, x, x + 0.0001)]
#
# res = []
# for a1 in ox:
#     for a2 in ox:
#         if a1 <= a2 and all(f(x) for x in ox):
#             res.append(a2 - a1)
# print(min(res))

# №7
# def f(x):
#     P = 10 <= x <= 80
#     Q = 30 <= x <= 50
#     A = a1 <= x <= a2
#     return A <= (P and not Q)
#
#
# ox = [dx for x in (10, 80, 30, 50) for dx in (x - 0.0001, x, x + 0.0001)]
#
# res = []
# for a1 in ox:
#     for a2 in ox:
#         if a1 <= a2 and all(f(x) for x in ox):
#             res.append(a2 - a1)
# print(max(res))

# №9
# def f(x):
#     P = 15 <= x <= 60
#     Q = 15 <= x <= 30
#     A = a1 <= x <= a2
#     return (not Q or P) and A
#
#
# ox = [dx for x in (15, 30, 60) for dx in (x - 0.01, x, x + 0.01)]
#
# res = []
# for a1 in ox:
#     for a2 in ox:
#         if a1 <= a2 and not all(f(x) for x in ox):
#             res.append(a2 - a1)
#             print(a1, a2, a2 - a1)
# print('---' * 10)
# print(min(res))

# № 10
# def f(x):
#     P = x in {1, 12}
#     Q = x in {12, 13,14, 15, 16}
#     A = x in a
#     return (not A) <= (not P and not Q)
#
# a = set()
# for x in range(1000):
#     if f(x) == False:
#         a.add(x)
# print(len(a), a)

# № 11
def f(x):
    P = x in {2, 4, 6,8, 10, 12, 14, 16, 18, 20}
    Q = x in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
    A = x in a
    return (A <= P) and (Q <= (not A))

a = set(range(500))
for x in range(500):
    if f(x) == False:
        a.remove(x)
print(len(a), a)