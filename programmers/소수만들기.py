from itertools import combinations
def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for i in range(len(combi)):
        num = sum(combi[i])
        prime = 0
        for j in range(2, num):
            if(num%j == 0):
                prime = 1
        if(prime == 0):
            answer += 1
    return answer

nums = [1,2,7,6,4]
print(solution(nums))