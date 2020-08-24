T=int(input())
for test_case in range(1, T+1):
    N, M=map(int, input().split())
    oven=[0 for _ in range(N)]
    pizza_start=0
    pizza_finish=0
    front=0
    pizza_list=list(map(int, input().split()))
    for i in range(N):
        oven[i]=[pizza_list[i], i]
    pizza_start+=N
    while(pizza_finish!=M-1):
        if(front==N):
            front=0
        if(oven[front][0]==0):
            front+=1
            continue
        oven[front][0]=oven[front][0]//2
        if(oven[front][0]==0):
            pizza_finish+=1
            if(pizza_start!=M):
                oven[front]=[pizza_list[pizza_start], pizza_start+1]
                pizza_start+=1
        front+=1
    oven.sort(key=lambda x:x[0])
    print("#{0} {1}".format(test_case, oven[N-1][1]))
    
