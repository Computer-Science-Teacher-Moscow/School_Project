with open('9.txt', 'r') as file:
    sm = 0
    for i, nums in enumerate(file, 1):
        nums = list(map(int, nums.split()))
        nums_rep_4 = [x for x in nums if nums.count(x) == 4]
        nums_free = [x for x in nums if nums.count(x) == 1]
        if nums_rep_4 and len(nums_free) == 3 and nums == sorted(nums):
            sm += i
            print(*nums)
print('-----')
print(sm)