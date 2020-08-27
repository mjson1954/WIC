T = int(input())

for tc in range(1, T+1):
    day, month, threeMonth, year = map(int, input().split()) # 이용 요금
    plan = list(map(int, input().split())) # 수영장 이용 계획
    flag = [0 for _ in range(12)] # 0:day, 1: month, 2: threemonth
    threemonth_count = 0
    month_count = 0
    cnt = 0
    count = 0
    
    for i in range(10):
        if(cnt == 0):
            temp = (plan[i] + plan[i+1] + plan[i+2]) * day
            if(temp > threeMonth):
                threemonth_count += 1
                flag[i] = 2
                flag[i+1] = 2
                flag[i+2] = 2
                cnt = 2
        else:
            cnt -= 1
            continue

    for i in range(12):mm
        if(flag[i] != 2 and plan[i] * day > month):
            month_count += 1
            flag[i] = 1

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

    print(flag)
    print("#{0} {1}".format(tc, result))

