n = int(input())
res = []
# cnt = 0
for _ in range(n):
    a = int(input())
    if a % 7 == 1:
        res.append(a)
        # cnt +=1
if res:
    print(len(res))
else:
    print('NO')
