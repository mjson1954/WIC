T=int(input())
def partition(card, i, j, tmp):
    global result
    global count
    left=card[i:(i+j)//2+1]
    right=card[(i+j)//2+1:]
    if(tmp==-1):
        result[0]=left
        result[1]=right
        count[0]+=1
        count[1]+=1
    else:
        if(tmp==0):
           result[0]=[left, right]
           count[0]+=1
        else:
            result[1]=[left, right]
            count[1]+=1
    if(len(left)>3):
        partition(left, 0, len(left)-1, 0)
    if(len(right)>3):
        partition(right, 0, len(right)-1, 1)
def cal(tmp0, tmp1):
    if(tmp0==1 and tmp1==2):
        return tmp1
    elif(tmp0==1 and tmp1==3):
        return tmp0
    elif(tmp0==2 and tmp1==1):
        return tmp0
    elif(tmp0==2 and tmp1==3):
        return tmp1
    elif(tmp0==3 and tmp1==1):
        return tmp1
    elif(tmp0==3 and tmp1==2):
        return tmp0
    else:
        return tmp0
    
def inside(result, count):
    global temp
    Count=count
    if(count==1):
        temp.append(result)
    while(count!=1):
        tmp=result[0]
        temp.append(tmp)
        
        count-=1
    while(Count!=1):
        tmp=result[1]
        temp.append(tmp)
        Count-=1

    
for test_case in range(1,T+1):
    num=int(input())
    card=list(map(int, input().split()))
    count=[0,0]
    result=[0,0]
    results=[]
    partition(card, 0, len(card)-1, -1)
    print(result)
    print(len(result))
    print(count)
    temp=[]
    inside(result[0], count[0])
    inside(result[1], count[1])   
    print(temp)
    for i in range(len(temp)):
        if(len(temp[i])==2):
            s=cal(temp[i][0], temp[i][1])
            results.append(s)
        else:
            s=cal(temp[i][0], temp[i][1])
            ss=cal(s, temp[i][2])
            results.append(s)
    print(results)
