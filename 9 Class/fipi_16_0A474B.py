n = int(input())
res = []
for _ in range(n):
    a = int(input())
    if a % 7 in [1,3,5,7,9]:
        res.append(a)
if res:
    print(sum(res)/len(res))
else:
    print('NO')