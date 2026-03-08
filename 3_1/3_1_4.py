with open('3_1_4.txt', 'r') as file:
    cnt = 0
    for s in file:
        l = sorted(map(int, s.split()))
        if sum(l[:-1]) > l[-1] and len(set(l)) == len(l) - 1:
            cnt += 1
            print(*l)
print(cnt)
