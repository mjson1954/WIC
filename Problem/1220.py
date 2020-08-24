for test_case in range(1, 11):
    N=int(input())
    table=[[] for i in range(N)]
    for i in range(N):
        line=list(map(int, input().split()))
        for j in range(N):
            table[j].append(line[j])
# print(table)
    count=0
    for i in range(N):
        status=0
        for j in range(N):
            if(table[i][j]==0):
                pass
            elif(table[i][j]==1 and status==0): #01
                status=1
            elif(table[i][j]==1 and status==1): #11
                pass 
            elif(table[i][j]==2 and status==0): #02
                pass
            elif(table[i][j]==2 and status==1): #12
                count+=1
                status=0
            else:
                pass
    print("#{0} {1}".format(test_case, count))