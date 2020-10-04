def solution(priorities, location):
    answer = 0
    count = 0
    n = len(priorities)
    idx = 0
    while(count < n):
        temp = priorities[idx]
        if(idx == len(priorities)-1):
            count += 1
            answer = count
            continue
        if(temp < max(priorities[idx+1:])):
            priorities.append(temp)
        else:
            count += 1
            if(idx % n == location):
                answer = count
                break
        idx += 1

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))