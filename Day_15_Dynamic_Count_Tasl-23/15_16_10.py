# Рекурсивный подход
def f(curr, end, cnt=0):
    if curr == 15 or curr == 21: cnt += 1
    if curr > end: return 0
    if curr == end: return cnt == 1
    return f(curr + 1, end, cnt) + f(curr +2, end, cnt) + f(curr * 3, end, cnt)

# # Рекурсивный подход
# def f(curr, end, cnt=0):
#     if curr == 15 or curr == 21: cnt += 1
#     if curr > end: return 0
#     if curr == end: return cnt == 0
#     return f(curr + 1, end, cnt) + f(curr +2, end, cnt) + f(curr * 3, end, cnt)
#
# print(f(6, 25))
#
# def f(curr, end):
#
#     if curr > end or curr == 15 or curr == 21: return 0
#     if curr == end: return 1
#     return f(curr + 1, end) + f(curr +2, end) + f(curr * 3, end)
#
# print(f(6, 25))