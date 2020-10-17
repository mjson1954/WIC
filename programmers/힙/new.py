import heapq

def solutions(jobs):
    answer = 0
    sec = -1 # 현재시각
    count = 0 # 끝난 작업 수
    n = len(jobs) # 작업의 개수
    inlist = []
    flag = 0
    while(count < n):
        sec += 1 
        # 1. 현재 시각에 들어온 작업이 있나?
        del_list = []
        if(len(jobs) > 0):
            for i in range(len(jobs)):
                if(jobs[i][0] == sec):
                    heapq.heappush(inlist, [jobs[i][1], jobs[i][0]])
                    del_list.append(i)
            for i in range(len(del_list)):
                del jobs[i]
        
        # 2. 현재 작업할 수 있는 것 파악 -> 작업 시작
        if(flag == 0 and len(inlist) > 0):
            end = sec + inlist[0][0]
            

        # 3. 현재 시각에 끝나는 작업이 있나?
        if(sec >= end and len(inlist) > 0 and flag == 1):
            start = heapq.heappop(inlist)[1]
            answer += (end - start)
            count += 1
            flag = 0

    return int(answer / n)
    
                


jobs = [[0,3], [0,2], [1,9], [2,6]]
print(solutions(jobs))