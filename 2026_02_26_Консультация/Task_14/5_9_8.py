from string import printable


def num_to_10(num: str, cs: int) -> int:
    return sum(printable[:cs].index(x) * cs ** i for i, x in enumerate(num[::-1]))


for x in printable[:37][::-1]:
    a = num_to_10(f'c59{x}ba98f', 37)
    b = num_to_10(f'e3{x}5da9c6', 37)
    if not a * b % 36:
        print(num_to_10(f'2{x}1', 37))
        break



# from string import printable


# def num_to_10(num: str, cs: int) -> int:
#     return sum(printable[:cs].index(x) * cs ** i for i, x in enumerate(num[::-1]))

# def num_to_10(num: str, cs: int) -> int:
#     print(num)
#     res = []
#     for i, x in enumerate(num[::-1]):
#         print(i, x)
#         res.append(printable[:cs].index(x) * cs ** i)
#         print(printable[:cs].index(x) * cs ** i, f'{printable[:cs].index(x)} * {cs} ** {i}')
#         print(printable[:cs], '"printable[:cs]"')
#         print(printable[:cs].index(x), '"printable[:cs].index(x)"')
#     print(*res)
#     print(sum(res))
#     input()
#     print('-----')
#
#
#     # return sum(printable[:cs].index(x) * cs ** i for i, x in enumerate(num[::-1]))
#
# for x in printable[:37][::-1]:
#     a = num_to_10(f'c59{x}ba98f', 37)
#     b = num_to_10(f'e3{x}5da9c6', 37)
#     if not a * b % 36:
#         print(num_to_10(f'2{x}1', 37))
#         break