with open('5_38_8_17-407.txt') as file:
    a = [int(x) for x in file]

res = []
cnt_k32 = sum(abs(x) % 32 == 0 for x in a)
print(cnt_k32)

for pr in zip(a, a[1:]):
    if any(x < 0 for x in pr) and (sm:=sum(pr)) < cnt_k32:
        res.append(sm)
        print(*pr)
print(len(res), max(res))

