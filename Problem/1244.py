import copy
T=int(input())
for test_case in range(1, T+1):
    num, count=input().split()
    num=list(num)
    tmp=list(map(int, num))
    tmp.sort(reverse=True)
    tmp=list(map(str, tmp))
    maxnum=''.join(tmp)
    count=int(count)
    result=[num]
    for c in range(count):
        # 완전탐색
        temp_result=result
        if(c>0):
            for i in range(len(temp_result)):
                temp_result[i]=list(temp_result[i])
        result=[]
        shoot=True
        for x in range(len(temp_result)):
            start=1
            for i in range(len(temp_result[x])):
                for j in range(start, len(temp_result[x])):
                    n=copy.deepcopy(temp_result[x])
                    #print(i ,j)
                    temp=temp_result[x][j]
                    temp_result[x][j]=temp_result[x][i]
                    temp_result[x][i]=temp
                    new=''.join(temp_result[x])
                    result.append(''.join(temp_result[x]))
                    temp_result[x]=n
                    if(new==maxnum):
                        shoot=False
                        break
                start+=1
                print(result)
                if(shoot==False):
                    break
            if(shoot==False):
                break
            #print("c: ",c," x: ",x, " result: ",result)
    if(shoot==False):
        print("#{0} {1}".format(test_case, maxnum))
    else:
        print("#{0} {1}".format(test_case, max(result)))
    
