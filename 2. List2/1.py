T= int(input())
for test_case in range(1, T+1):
    coloring=[[0,0,0,0,0,0,0,0,0,0] for i in range(10)]
    count=0
    N=int(input())
    for i in range(N):
        num=input().split()
        for i in range(len(num)):
            num[i]=int(num[i])
        for i in range(num[0], num[2]+1):
            for j in range(num[1], num[3]+1):
                coloring[i][j]+=num[4]
    for i in range(10):
        for j in range(10):
            if(coloring[i][j]==3):
                count+=1
    print("#{0} {1}".format(test_case, count))
        
    
