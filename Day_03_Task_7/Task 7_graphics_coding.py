# size = h * w (h и w - количество пикселей по вертикали и горизонтали)
# i - количество бит, которой закодировано изображение
# v = size * i - объем информации, содержащейся в графическом файле (в битах)
# k = 2 ** i - количество цветов
# i = ceil(log2(k)) - определение разрядности кодирования, зная количество цветов

# №1
# size = 128 * 128
# i = 7
# v = size * i // 2 ** 13
# print(v)

# # №2
# from math import ceil
# size = 4000 * 6000
# i = 24
# v = size * i / 2 ** 23
# print(ceil(v))

# №3
# from math import ceil
# size = 800 * 600
# V = 600 * 2 ** 13
# for i in range(1,1000):
#     if size * i > V:
#         print(2 ** (i - 1))
#         break

# # №4
#
# size = 768 * 600
# V = 420 * 2 ** 13
# for i in range(1,1000):
#     if size * i > V:
#         print(2 ** (i - 1))
#         break

# №5
# from math import ceil
#
# size = 1024 * 768
# v_add = 640 * 2 ** 13
# N = 2048
# V = 2 * 2 ** 33
# for i in range(1, 1000):
#     if (size * i + v_add) * N > V:
#         print(2 ** (i - 1))
#         break

# # №6
# size = 1024 * 768
# i = 12
# N = 256
# v = size * i
# V = v * N // 2 ** 23
# print(V)

# # №7
# size = 486 * 720
# V = 80 * 2 ** 13
# for i in range(1,300):
#     if .85 * size * i > V:
#         print(2 ** (i - 1))
#         break

# №9
# size = 640 * 256
# V = 170 * 2 ** 13
# for i in range(1,300):
#     if size * i /1.35 > V:
#         print(2 ** (i - 1))
#         break

# # №10
# size = 1280 * 1024
# i = 10
# N = 220
# tr_sp = 12_582_912
# v = size * i
# v_packet = v * N
# t = v_packet // tr_sp
# print(t)

# # №11
# size = 1024 * 768
# i = 23
# size_1 = 800 * 600
# i_1 = 22
# N = 100
# v = size * i
# v_c = size_1 * i_1
# d_tr = (v - v_c) * 100
# print(d_tr // 2 ** 13)

# # №13
# size = 1280 * 960
# i = 11
# tr_sp = 96_468_992
# t = 132
# v = size * i
# for N in range(1000):
#     if v * N / tr_sp > t:
#         print(N - 1)
#         break

# №14
size = 1280 * 1024
N = 39
tr_sp = 1966080
t = 280
for i in range(1, 1000):
    if size * i * N / tr_sp > t:
        print(2 ** (i - 1))
        break

# №14 вариант решения 2
from math import ceil, log2
size = 1280 * 1024
N = 39
tr_sp = 1966080
t = 280
for color in range(5000, 1, -1):
    if size * ceil(log2(color)) * N / tr_sp <= t:
        print(color)
        break
