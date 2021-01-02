def solution(citations):
    citations.sort()
    h = 0
    k = 0
    answer = 0
    for i in range(citations[-1]+1):
        h = sum(j>=i for j in citations) # i 번 이상 인용된 논문수 h
        k = sum(j<=i for j in citations) # i 번 이하 인용된 논문수 k
        if(h >= i and k <= i): # h가 i이상이고 k가 i이하인 조건을 만족하는 값
            if(i > answer):
                answer = i # 그 중에 최대값을 구함
    if(citations[0]>=len(citations)):
        answer = len(citations)
    return answer