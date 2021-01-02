T=int(input())
monthEnd=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T+1):
    count=1
    startMonth, startDay, endMonth, endDay=map(int, input().split())
    if(startMonth==endMonth):
        count+=endDay-startDay
    else:
        for i in range(startMonth+1, endMonth):
            count+=monthEnd[i]
        count+=monthEnd[startMonth]-startDay
        count+=endDay
    print("#{0} {1}".format(test_case, count))