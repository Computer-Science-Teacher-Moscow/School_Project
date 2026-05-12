# n = int(input())
#
# cnt = 0
# sm = 0
# for _ in range(n):
#     a = int(input())
#     if a >= 15:
#         cnt += 1
#         sm += a
# if cnt:
#     print(sm/cnt)
# else:
#     print('Я не умею делить на ноль. А вы?')
from locale import windows_locale

# n = int(input())
#
# s = []
# for _ in range(n):
#     a = int(input())
#     if a >= 15:
#         s.append(a)
#         print((s))
# print(min(s), print(max(s)))
# if s:
#     print(sum(s) / len(s))
# else:
#     print('Я не умею делить на ноль. А вы?')

# n = int(input())
# res = []
# for _ in range(n):
#     a = int(input())
#     if (9 < a < 100) and (a % 3 == 0 or a % 10 == 3):
#         res.append(a)
# print(sum(res)/len(res) - len(res))

def f():
    a = int(input())
    res = []
    while a:
        if a % 7 == 0:
            res.append(a)
        a = int(input())
    if res:
        print(round(sum(res)/len(res), 2))
    else:
        print('НЕТ')

a = 6
b = 7
print(a+b)
