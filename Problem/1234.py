def check(num):
    result=[]
    count=0
    pos=0
    for i in range(len(num)):
        if(i==len(num)-1 and count==0):
            result.append(num[len(num)-1])
        elif(i==len(num)-1 and count==1):
            pass
        else:
            if(num[i]!=num[i+1] and count==0):
                result.append(num[i])
            elif(count==1):
                count=0
                result.append(num[i+1:])
                break
            else:
                pos=1
                count=1
    if(pos==0):
        return -1
    else:
        return ''.join(result)

for test_case in range(1, 11):
    N, num=input().split()
    N=int(N)
    while(1):
        temp=check(num)
        # print(temp)
        if(temp==-1):
            break
        else:
            num=check(num)
    print("#{0} {1}".format(test_case, num))


