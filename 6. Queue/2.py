dx=[-1,0,1,0] 
dy=[0,1,0,-1]
def process(start, end):
    global count
    now=[start[0], start[1]]
    checklist=[]
    if(maze[now[0]][now[1]]==3):
        return
    else:
        for i in range(4):
            testX=now[0]+dx[i]
            testY=now[1]+dy[i]
            if(testX>N-1 or testY>N-1 or testX<0 or testY<0):
                continue
            if(maze[testX][testY]==0):
                checklist.append([testX, testY])
    print("checklist: ", checklist)
    while(checklist):
        now=checklist[0].pop()
        count+=1
        process(start, end)


    
T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    maze=[]
    count=0
    for i in range(N):
        line=input()
        temp=[int(line[i]) for i in range(len(line))]
        maze.append(temp)
    start=[N-1, maze[N-1].index(2)]
    end=[0, maze[0].index(3)]
    print(start, end)
    process(start, end)
    print(count)
    