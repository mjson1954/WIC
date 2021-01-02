def solution(n, times):
    answer = -1
    minTime = 1
    maxTime = n * max(times)
    
    while(minTime <= maxTime):
        avgTime = (maxTime + minTime) // 2
        human = 0
        for time in times:
            human += avgTime // time
            
        if(human >= n):
            if(answer == -1):
                answer = avgTime
            else:
                answer = min(answer, avgTime)
            maxTime = avgTime - 1
        elif(human < n):
            minTime = avgTime + 1
      
    return answer