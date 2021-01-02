import heapq

def solution(scoville, K):
    answer = 0
    flag = 0
    heapq.heapify(scoville)
    
    while(flag == 0):
        if(len(scoville) == 1 and scoville[0] < K ):
            answer = -1
            break
        if(scoville[0] < K):
            min_fir = heapq.heappop(scoville)
            min_sec = heapq.heappop(scoville)
            new = min_fir + min_sec * 2
            heapq.heappush(scoville, new)
            answer += 1
        else:
            flag = 1
        
    return answer


scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville, K))