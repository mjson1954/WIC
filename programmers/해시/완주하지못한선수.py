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

#********** collection 모듈 사용 *********

# import collections


# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]