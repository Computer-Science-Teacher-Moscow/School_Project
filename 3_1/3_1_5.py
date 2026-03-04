with open('3_1_5.txt') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        if len(set(l)) == 5 and 2 * (l[0] + l[-1]) >= sum(l[1:-1]):
            cnt += 1
            print(*l)
print(cnt)
