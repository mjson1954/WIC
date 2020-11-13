from itertools import combinations

while(1):
    nums = list(map(int, input().split()))
    if(nums[0] == 0):
        break
    del nums[0]
    nums.sort()
    for x in list(combinations(nums, 6)):
        for j in x:
            print(j, end=' ')
        print()
    print()