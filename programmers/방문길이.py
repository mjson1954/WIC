visit = [] # set
def up(now):
    now[1] += 1
    flag = 0
    if(now[1] > 5):
        now[1] = 5
    else:
        if(not(now in visit)):
            flag = 1
            visit.append(now)
    return now, flag

def down(now):
    now[1] -= 1
    flag = 0
    if(now[1] < -5):
        now[1] = -5
    else:
        if(not([now[0], now[1]+1] in visit)):
            flag = 1
            visit.append([now[0], now[1]+1])
    return now, flag

def right(now):
    now[0] += 1
    flag = 0
    if(now[0] > 5):
        now[0] = 5
    else:
        if(not(now in visit)):
            flag = 1
            visit.append(now)
    return now, flag

def left(now):
    now[0] -= 1
    flag = 0
    if(now[0] < -5):
        now[0] = -5
    else:
        if(not([now[0]+1, now[1]] in visit)):
            flag = 1
            visit.append([now[0]+1, now[1]])
    return now, flag

def solution(dirs):
    answer = 0
    now = [0, 0]
    for direc in dirs:
        if(direc == 'U'):
            now, flag = up(now)
        elif(direc == 'D'):
            now, flag = down(now)
        elif(direc == 'R'):
            now, flag = right(now)
        else:
            now, flag = left(now)
        if(flag == 1):
            answer += 1


    return answer

dirs = "ULURRDLLU"
print(solution(dirs))