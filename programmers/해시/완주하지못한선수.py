def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append(' ')
    for i in range(len(participant)):
        if(participant[i]!=completion[i]):
            answer = participant[i]
            break
            
    return answer