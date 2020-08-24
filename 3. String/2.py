T=int(input())
for test_case in range(1, T+1):
    num=input().split(' ')
    for i in range(len(num)):
        num[i]=int(num[i])
    mylist=[input().split() for _ in range(num[0])] #2차원 배열 생성
    for i in range(num[0]):
        for j in range(num[0]-num[1]+1):
            temp1=mylist[i][0][j:num[1]+j]
            temp2=temp1[::-1]
            if(temp1==temp2):
                print("#{0} {1}".format(test_case, temp1))
    mylist2=[[] for _ in range(num[0])]
    for i in range(num[0]):
        for j in range(num[0]):
            mylist2[j].append(mylist[i][0][j])
            #세로 줄 넣은 2차원 배열 생성
    for i in range(num[0]):
        for j in range(num[0]-num[1]+1):
            temp="".join(mylist2[i])
            temp1=temp[j:num[1]+j]
            temp2=temp1[::-1]
            if(temp1==temp2):
                print("#{0} {1}".format(test_case, temp1))

    

    
    
    
