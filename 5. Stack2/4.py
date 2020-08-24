def find(num):
    global N
    global count
    visit=[0 for i in range(N)]
    for i in range(N):
        print("#",i)
        m=min(num[i])
        midx=[i for i,j in enumerate(num[i]) if j==m]
        temp_count=[0 for i in range(len(midx))]
        print(midx)
        for x in range(len(midx)):
            if(visit[num[i][midx[x]]]==0):
                temp_count[x]+=m
                visit[midx[x]]=1
                break
            else:
                tmp=10
                for j in range(N):
                    if(visit[j]==0):
                        if(num[i][j]<tmp):
                            tmp=num[i][j]
                    else:
                        pass
                temp_count[x]+=tmp
                visit[num[i].index(tmp)]=1
        print(temp_count)
        count=min(temp_count)
        print(visit)


T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    num=[]
    count=0
    for i in range(N):
        tmp=list(map(int, input().split()))
        num.append(tmp)
    find(num)
    print(count)
    
