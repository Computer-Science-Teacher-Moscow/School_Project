# Рекурсивный подход
def f(curr, end, step='0'):
    if curr > end: return 0
    if curr == end: return 1
    if step == '**2':
        return f(curr + 2, end, '+2') + f(curr * 3, end, '*3')
    return f(curr + 2, end, '+2') + f(curr * 3, end, '*3') + f(curr ** 2, end, '**2')


print(f(2, 64))
