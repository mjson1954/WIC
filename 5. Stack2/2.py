T=int(input())
dx=[0,1,0,-1] #상하좌우
dy=[1,0,-1,0]
    
for test_case in range(1, T+1):
    N=int(input())
    maze=[]
    for i in range(N):
        line=input()
        temp=[int(line[i]) for i in range(len(line))]
        maze.append(temp)
    start=[N-1, maze[N-1].index(2)]
    end=[0, maze[0].index(3)]
    print("start end:", start, end)
    now=start
    print("now:",now)
    pre=[-1, -1]
    while(now!=end):
        result=0
        for i in range(4):
            testX=now[0]+dx[i]
            testY=now[1]+dy[i]
            if(testX<0 or testY<0 or testX>N-1 or testY>N-1):
                continue
            else:
                if(maze[testX][testY]==0 and [testX, testY]!=pre and [testX, testY]!=now):
                    pre=now
                    now=[testX, testY]
                    result=1
                    break
                elif([testX, testY]==end):
                    print("길 있음")
                    result=1
                    now=end

        if(result==0):
            temp=now
            now=pre
            pre=temp
        elif(result==0 and [testX, testY]==start):
            print("길 없음")
            break
            
    print("최종", now)
    
    
