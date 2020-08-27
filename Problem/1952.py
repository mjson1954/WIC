T = int(input()) 

def allday(price, plan):
    return sum(plan) * price

def allmonth(price, plan):
    count = 0
    for i in range(12):
        if(plan[i]>0):
            count += 1
    return count * price

def allyear(price, plan):
    return price

def allthreemonth(price, plan):
    return price * 4

def threemonth_month(threemonth_price, month_price, plan):
    count = 0
    for i in range(12):
        if(plan[i] > 0):
            count += 1
    threemonth_count = count // 3
    month_count = count % 3
    return threemonth_count*threemonth_price + month_count*month_price

def getlocation(plan):
    plan_list = []
    for i in range(len(plan)-2):
        amount = plan[i]+plan[i+1]+plan[i+2]
        plan_list.append(amount)
    idx = plan_list.index(max(plan_list))
    return idx
    

def threemonth_day(threemonth_price, day_price, plan):
    price_list = []
    
    # threemonth 1번 일때
    max_idx = getlocation(plan)
    plan_b = plan.copy()
    del plan_b[max_idx:max_idx+3]
    price_list.append(threemonth_price + day_price * sum(plan_b))

    # threemonth 2번 일때
    second_idx = getlocation(plan_b)
    plan_c = plan_b.copy()
    del plan_c[second_idx:second_idx+3]
    price_list.append(threemonth_price * 2 + day_price * sum(plan_c))

    # threemonth 3번 일때
    third_idx = getlocation(plan_c)
    plan_d = plan_c.copy()
    del plan_d[third_idx:third_idx+3]
    price_list.append(threemonth_price * 3 + day_price * sum(plan_d))

    return min(price_list)


def threemonth_month_day(threemonth_price, month_price, day_price, plan):
    price_list = []
    threshold = month_price // day_price
    # threemonth 1번 일때
    max_idx = getlocation(plan)
    plan_b = plan.copy()
    del plan_b[max_idx:max_idx+3]
    count = 0 
    day_count = 0
    for i in range(len(plan_b)):
        if(plan_b[i] > threshold):
            count += 1
        else:
            day_count += plan_b[i]
    price_list.append(threemonth_price + day_price * day_count + month_price * count)

    # threemonth 2번 일때
    second_idx = getlocation(plan_b)
    plan_c = plan_b.copy()
    del plan_c[second_idx:second_idx+3]
    count = 0 
    day_count = 0
    for i in range(len(plan_c)):
        if(plan_c[i] > threshold):
            count += 1
        else:
            day_count += plan_c[i]
    price_list.append(threemonth_price*2 + day_price * day_count + month_price * count)

    # threemonth 3번 일때
    third_idx = getlocation(plan_c)
    plan_d = plan_c.copy()
    del plan_d[third_idx:third_idx+3]
    count = 0 
    day_count = 0
    for i in range(len(plan_d)):
        if(plan_d[i] > threshold):
            count += 1
        else:
            day_count += plan_d[i]
    price_list.append(threemonth_price*3 + day_price * day_count + month_price * count)

    return min(price_list)

def day_month(day_price, month_price, plan):
    price_list = []
    plan = sorted(plan)
    count = 0
    for i in range(12):
        if(plan[i]>0):
            count += 1 # 출석 예정이 있는 달
    for i in range(1, count):
        temp1 = i*month_price
        plan_b = plan[0:len(plan)-i]
        temp2 = sum(plan_b) * day_price
        price_list.append(temp1 + temp2)
    return min(price_list)


for tc in range(1, T+1):
    day, month, threeMonth, year = map(int, input().split()) # 이용 요금
    plan = list(map(int, input().split())) # 수영장 이용 계획
    price_list = []
    price_list.append(allday(day, plan))
    price_list.append(allmonth(month, plan))
    price_list.append(allyear(year, plan))
    price_list.append(threemonth_month(threeMonth, month, plan))
    price_list.append(threemonth_day(threeMonth, day, plan))
    price_list.append(day_month(day, month, plan))
    price_list.append(threemonth_month_day(threeMonth, month, day, plan))
    # price_list.append(allthreemonth(threeMonth, plan))

    print(price_list)
    print("#{0} {1}".format(tc, min(price_list)))


