T=int(input())
for test_case in range(T):
    N=int(input())
    new=[]
    new.append(list(map(int, input().split())))
    for i in range(N-1):
        temp=list(map(int, input().split()))
        poss=1
        delList=[]
        for j in range(len(new)):
            if(new[j][0]<temp[0] and new[j][1]<temp[1]):
                poss=0
                break
            elif(new[j][0]>temp[0] and new[j][1]>temp[1]):
                poss=2
                delList.append(j)
            else:
                pass
        if(poss==1):
            new.append(temp)
        elif(poss==2):
            for s in range(len(delList)):
                del new[delList[s]]
            new.append(temp)
            delList=[]
    print(len(new))
