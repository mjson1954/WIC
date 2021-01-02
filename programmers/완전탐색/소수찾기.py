from itertools import permutations

def find(num):
    if(num != 1 and num != 0):
        for i in range(2, num):
            if(num % i == 0):
                return False
    else:
        return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    entire = []
    for i in range(1, len(numbers)+1):
        for j in list(permutations(numbers, i)):
            num = int(''.join(j))
            entire.append(num)
    entire = list(set(entire))
    for num in entire:
        if(find(num)):
            answer += 1
    return answer

print(solution("17"))