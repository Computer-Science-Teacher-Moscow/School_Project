a = [x for x in range(222,1000000, 222) if all(c in '02468' for c in str(x))]
a5 = (5 ** i for i in range(1, 10))
cnt = 0
for n in range(1_000_001, 10**10):
    for i in range(1,10):
        if any(5 ** i + x == n for x in a):
            print(n, i)
            cnt +=1
    if cnt == 5:
        exit()