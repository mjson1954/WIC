def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        percent = 100 - progresses[i]
        day = percent // speeds[i]
        if(percent % speeds[i] > 0):
            day += 1
        days.append(day)
    for i in range(1, len(days)):
        if(days[i-1] > days[i]):
            days[i] = days[i-1]
    cnt = 1
    for i in range(1, len(days)):
        if(days[i] == days[i-1]):
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer
    
print(solution([93, 30, 55], [1, 30, 5]))