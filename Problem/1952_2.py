T = int(input())

for tc in range(1, T+1):
    day, month, threeMonth, year = map(int, input().split()) # 이용 요금
    plan = list(map(int, input().split())) # 수영장 이용 계획
    flag = [-1 for _ in range(14)] # 0:day, 1: month, 2: threemonth
    cnt = 0
    
    plan.append(0)
    plan.append(0)
    print(plan)

    for i in range(12):
        flag[i] = 0
    
    for i in range(12):
        if(plan[i] * day > month):
            flag[i] = 1

    for i in range(12):
        if(cnt == 0):
            temp = []
            temp.append((plan[i] + plan[i+1] + plan[i+2]) * day)
            temp.append(month + (plan[i+1] + plan[i+2])*day)
            temp.append(month + (plan[i]+plan[i+2])*day)
            temp.append(month + (plan[i]+plan[i+1])*day)
            temp.append(month*2 + plan[i]*day)
            temp.append(month*2 + plan[i+1]*day)
            temp.append(month*2 + plan[i+2]*day)
            mintemp = min(temp)

            if(mintemp > threeMonth):
                flag[i] = 2
                flag[i+1] = 2
                flag[i+2] = 2
                cnt = 2
        else:
            cnt -= 1
            continue
    print(flag)
    result = 0
    for i in range(len(flag)):
        if(flag[i]==0):
            result += plan[i] * day
        elif(flag[i]==1):
            result += month
        elif(flag[i]==2):
            result += threeMonth
            flag[i+1] = -1
            flag[i+2] = -1
        else:
            pass
    
    if(year < result):
        result = year

    print("#{0} {1}".format(tc, result))

