def solution(d, budget):
    answer = 0
    d.sort()
    while(budget > 0 and len(d)>0):
        x = d.pop(0)
        budget -= x
        answer += 1
    if(budget < 0):
        answer -= 1
    return answer