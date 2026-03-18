# print(*'xywzF')
#
# for x in (0,1):
#     for y in (0,1):
#         for w in (0,1):
#             for z in (0,1):
#                 F = ((w <= y) <= x) or (not z)
#                 if not F:
#                     print(x, y, w, z, F)

print(*'xywzF')

for x in (0,1):
    for y in (0,1):
        for w in (0,1):
            for z in (0,1):
                F = ( not( y and (not x)) and (not(x ==z)) and w)
                if  F:
                    print(x, y, w, z, F)