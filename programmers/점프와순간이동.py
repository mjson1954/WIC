def solution(n):
    battery = 0
    while(n > 1):
        if(n % 2 == 0): # 짝수이면
            n = n//2
        else:
            n -= 1
            battery += 1
            n = n//2
    return battery+1

n = 5
print(solution(n))