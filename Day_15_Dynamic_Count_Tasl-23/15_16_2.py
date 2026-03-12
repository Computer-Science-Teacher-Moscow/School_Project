# Динамический подсчёт

f = [0] * 20
f[1] = 1
for i in range(1, 18):
    if i + 1 <= 18: f[i + 1] += f[i]  # i + 1 - возжная команда
    if i * 2 <= 18: f[i * 2] += f[i]  # i * 2 - возжная команда
    if i * 3 <= 18: f[i * 3] += f[i]  # i * 2 - возжная команда

print(f[18])
print(f)


# Рекурсивный подход
def f(curr, end):
    if curr > end: return 0
    if curr == end: return 1
    return f(curr + 1, end) + f(curr * 2, end) + f(curr * 3, end)


print(f(1, 18))
