import heapq

def solution(jobs):
    # jobs.sort()
    answer = 0
    count = 0
    sec = -1
    end = 0
    inlist = []
    while(count < len(jobs)):
        sec += 1
        for i in range(len(jobs)):
            if(jobs[i][0] == sec):
                heapq.heappush(inlist, [jobs[i][1], i])

        if(sec >= end or count == 0):
            job, i = heapq.heappop(inlist)
            end = job + sec # 끝나는 시각
            count += 1
            answer += (end - jobs[i][0])
        
    answer = answer / len(jobs)
    return int(answer)

jobs = [[0,3], [1,9], [2,6]]
print(solution(jobs))