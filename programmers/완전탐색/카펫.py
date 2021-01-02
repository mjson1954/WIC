def solution(brown, yellow):
    answer = []
    num = brown + yellow
    x = []
    for i in range(1, num+1):
        if(num % i == 0):
            x.append([i, num//i])
    for n in x:
        if((n[0]-2)*(n[1]-2) == yellow):
            answer = [n[0], n[1]]
            if(n[1] > n[0]):
                answer = [n[1], n[0]]
            break
    return answer
    

print(solution(24,24))