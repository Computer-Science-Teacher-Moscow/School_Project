# nu - частота дискредитации в кГц ( 1Гц - 1/с)
# i - разрешение аудио потока в битах
# t - время звучания
# k - количество каналов звучания
# v = nu * i * k * t

# №1
# k = 2
# i = 24
# nu = 48_000
# v = 288 * 2 ** 23
# t = v / (nu * i * k)/60
# print(t)

# №2
# k = 4
# i = 32
# nu = 32_000
# t = 2 * 60
# v = k * i * nu * t / 2 ** 23
# print(int(round(v,-1)))

# print(round(5.5), round(-5.5), round(4.5))

# # №3
# k = 2
# nu = 48_000
# t = 2 * 60 + 15
# V = 32 * 2 ** 23
# for i in range(1,560):
#     if k * nu * i * t > V:
#         print(i-1)
#         break

# # №4
# k = 2
# nu = 48_000
# i = 34
# N = 13
# t = 42 * 60 + 20
# v_zag = 110 * 2 ** 13
# v_audio = k * nu * i * t
# v_alb = v_audio + v_zag * N
# tr_sp = 314_572_800
# t_tr = v_alb // tr_sp
# print(t_tr)

# №8
# k = 2
# nu = 64_000
# i = 16
# t = 4 * 60
# v = k * i * nu * t
# v_c = .75 * v
# print(v_c / 2 ** 23)
