# Рекурсивный подход
def f(curr, end):
    if curr < end or curr == 28: return 0
    if curr == end: return 1
    if curr % 2 == 0:
        return f(curr - 2, end) + f(curr // 2, end)
    return f(curr - 2, end) + f(curr - 3, end)

print(f(98, 1))
