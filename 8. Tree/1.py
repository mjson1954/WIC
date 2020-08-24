T=int(input())
for test_case in range(1, T+1):
    E, N=map(int, input().split())
    edge=list(map(int, input().split()))
    result=0
    checkList=[N]
    for i in range(E):
        for j in range(len(checkList)):
            if(edge[2*i]==checkList[j]):
                result+=1
                checkList.append(edge[2*i+1])
                
    print("#{0} {1}".format(test_case, result+1))
