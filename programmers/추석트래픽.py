# 2018 카카오 신입 공채 코딩테스트 7번 (난이도 : 상)
#### 나중에 다시 풀기 ###

def calcTime(h, m, s, delay):
    h, m, s, delay = int(h), int(m), int(s), int(delay)
    if(s < delay):
        m -= 1
        if(m < 0):
            m = 59
            h -= 1
        s += 60.0
    return [h, m, s-delay+0.001]

def solution(lines):
    for line in lines:
        traffic = []

        date, time, delay = line.split()

        delay = delay[:-1]
        h, m, s = time.split(':')
        traffic.append([calcTime(h, m, s, delay), [int(h), int(m), int(s)]])
