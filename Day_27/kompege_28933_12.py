command = {(' ', 0): (' ', 1, 1),
            (' ', 1): ('1', 1, 2),
            ('0', 1): ('0', 1, 1),
            ('1', 1): ('1', 1, 1),
            (' ', 2): ('1', 1, 3),
            (' ', 3): (' ', 2, 3),
            }


def mt(s: str):
    s = list(f' {s}   ')
    print(s)
    q = 0
    i = 0
    while True:
        cmd_t = command[(s[i], q)]
        s[i] = cmd_t[0]
        if cmd_t[1] == 2:
            break
        i += cmd_t[1]
        q = cmd_t[2]
    return ''.join(s)

print(int(mt(bin(2027)[2:]), 2))
