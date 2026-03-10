from statistics import mean

cnt = 0
with open('3_6_4.txt') as file:
    for s in file:
        l = [int(x) for x in s.split()]
        l_rep_2 = [x for x in l if l.count(x) == 2]
        l_fr = [x for x in l if l.count(x) == 1]
        if len(set(l_rep_2)) == 1 and len(l_fr) == 4 and mean(l_fr) <= sum(l_rep_2):
            cnt+=1
print(cnt)

