T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    result=0
    cost=[]
    for i in range(N):
        cost.append(list(map(int, input())))
    # print(cost)
    size=N//2 # 어디서부터 더해야하는지
    count=1 # 몇개 더해야하는지
    increase=1
    for i in range(N):
        temp=0
        start=size
        for j in range(N):
            if(temp==count):
                break
            result+=cost[i][start]
            temp+=1
            start+=1
        # print(i,":",result)
        if(count==N):
            increase=0
        if(increase==1):
            count+=2
            size-=1
        else:
            count-=2
            size+=1
    print("#{0} {1}".format(test_case, result))
