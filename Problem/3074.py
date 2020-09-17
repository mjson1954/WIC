def solution(M, times):
    answer = -1
    minTime = 1
    maxTime = M * max(times)
    while(minTime <= maxTime):
        human = 0
        avgTime = (minTime + maxTime) // 2
        for time in times:
            human += avgTime // time
        if(human >= M):
            if(answer == -1):
                answer = avgTime
            else:
                answer = min(answer, avgTime)
            maxTime = avgTime - 1
        elif(human < M):
            minTime = avgTime + 1

    return answer



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    times = []
    for i in range(N):
        times.append(int(input()))
    print("#{0} {1}".format(tc, solution(M, times)))