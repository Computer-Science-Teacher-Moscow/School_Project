from math import dist

a = [(9,(5,6)),(10,(4,8)),(4,(4,19)),(15,(1,18)),(10,(5,15)),(15,(3,8)),(15,(6,6)),(7,(7,8))]

max_point = max(a)
print(max_point)
max_point_2el_tup = max(a, key=lambda x: x[1][1])
print(max_point_2el_tup)
max_el_cnt_min_dist_00 = max(a, key=lambda x: (x[0], -dist(x[1], (0,0))))
print(max_el_cnt_min_dist_00)
sep1 = '*'
sep2 = '#'
p = 0

