# № 1
# from  math import ceil, log2
# k = 10 + 1234
# i = ceil(log2(k))
# N = 65_536
# V = 2050 * 2 ** 10
# for n in range(1, 1000):
#     if (i * n / 8) * N > V:
#         print(n - 1)
#         break

# № 2
# from  math import ceil, log2
# k = 10 + 52 + 458
# i = ceil(log2(k))
# N = 862
# V = 276 * 2 ** 10
# for n in range(1, 1000):
#     if ceil(n *  i/ 8) * N > V:
#         print(n - 1)
#         break

# № 3
# from  math import ceil, log2
# k = 10 + 52 + 450
# i = ceil(log2(k))
# N = 708
# V = 213 * 2 ** 10
# for n in range(1, 1000):
#     if ceil(n *  i/ 8) * N > V:
#         print(n)
#         break

# # № 4
# from  math import ceil, log2
#
# n = 80
# N = 1200
# V = 150 * 2 ** 10
# for i in range(1, 1000):
#     if ceil(n *  i/ 8) * N > V:
#         print(2 ** (i - 1))
#         break

# # № 5
# from  math import ceil, log2
#
# n = 261
# N = 252_500
# V = 31 * 2 ** 20
# for i in range(1, 1000):
#     if ceil(n *  i/ 8) * N > V:
#         print(2 ** (i - 1) + 1)
#         break

# # # № 6
# from  math import ceil, log2
#
# n = 1231
# N = 523_872
# V = 432 * 2 ** 20
# for i in range(1, 1000):
#     if ceil(n *  i/ 8) * N > V:
#         print(2 ** (i - 1) + 1)
#         break

# # № 7
# from  math import ceil, log2
#
# n = 248
# N = 75_600
# V = 16 * 2 ** 20
# for i in range(1, 1000):
#     if ceil(n *  i/ 8) * N > V:
#         print(2 ** (i - 1) + 1)
#         break

# # # № 8
# from  math import ceil, log2
#
# size = 1280 * 1024
# n = 39
# tr_sp = 1_966_080
# t_tr = 280
# for i in range(1, 1000):
#     if size * i * n / tr_sp > t_tr:
#         print(2 ** (i - 1))
#         break

#  №9
# from  math import ceil, log2
#
# size = 7680 * 4320
# i = 16
# v_flash = 9 * 2 ** 33
# n_photos = 4010
# v_photo = size * i
# n_to_flash = v_flash // v_photo
# n_last_flash = n_photos % n_to_flash
# print(n_last_flash)

# # № 10
# size = 1024 * 120
# v = 210 * 2 ** 13
# i_transp = 7
# for i_color in range(1,1000):
#     # i = i_color + i_transp
#     if size * (i_color + i_transp) > v:
#         print(2 ** (i_color - 1))
#         break

# № 11
# size = 480 * 768
# v = 405 * 2 ** 13
#
# for i in range(1,1000):
#     if size * (i + i // 2 + i % 2) > v:
#         print(2 ** (i - 1))
#         break

# # № 12
# size = 800 * 640
# i = 12
# v = size * (i + i // 3 + (1 if i % 3 else 0))
# print(v // 2 ** 13)

# № 13
# size = 1024 * 120
# V = 210 * 2 ** 13
# for i in range(1000):
#     if size * (i + 1) > V:
#         print(2 ** (i - 1))
#         break

# № 13
# size = 1280 * 960
# i = 11
# tr_sp = 96_468_992
# t_tr = 132
# for n in range(1000):
#     if size * i * n / tr_sp > t_tr:
#         print(n - 1)
#         break