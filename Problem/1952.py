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

def threemonth_month(threemonth_price, month_price, plan):
    count = 0
    for i in range(12):
        if(plan[i] > 0):
            count += 1
    threemonth_count = count // 3
    month_count = count % 3
    return threemonth_count*threemonth_price + month_count*month_price

def threemonth_day(threemonth_price, day_price, plan):
    price_list = []
    count = 0
    for i in range(12):
        if(plan[i]>0):
            count += 1 # 출석 예정이 있는 달
    threemonth_count = count // 3 # 세달씩 묶을 수 있는 수
    for i in range(1, threemonth_count+1):
        temp1 = i*threemonth_price # 세달씩 묶는 요금 / 항상 일정
        # 여기 바꿔야함
        # 3달이 어떻게 들어갈지. 순서.
        plan_b = plan[0:len(plan)-i*3] # 1일 씩 내는 리스트
        temp2 = sum(plan_b) * day_price
        price_list.append(temp1 + temp2)
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
    print(price_list)
    print("#{0} {1}".format(tc, min(price_list)))


