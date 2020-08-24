T=int(input())
result=0
def push(item):
    s.append(item)
    
def pop():
    if len(s)==0:
        #underflow
        return
    else:
        return s.pop(-1) #마지막 위치의 값 삭제 and return

def search_1(now):
    global result
    if(maze[now[0]-1, now[1]]==0 and now[0]-1>=0):
        push([[now[0]-1, now[1]], 1)
        now=[now[0]-1, now[1]]
        go=1
    else:
        if(now==end):
            result=1
        else:
            temp=pop()
            now=temp[0]
            direction=temp[1]
            go=0
    return go
    
def search_2(now):
    global result
    if(maze[now[0], now[1]+1]==0 and now[1]+1<N):
        push([[now[0], now[1]+1], 2)
        now=[now[0], now[1]+1]
        go=1
    else:
        if(now==end):
            result=1
        else:
            temp=pop()
            now=temp[0]
            direction=temp[1]
            go=0
    return go
def search_3(now):
    global result
    if(maze[now[0]+1, now[1]]==0 and now[0]+1<N):
        push([[now[0]+1, now[1]], 3)
        now=[now[0]+1, now[1]]
        go=1
    else:
        if(now==end):
            result=1
        else:
            temp=pop()
            now=temp[0]
            direction=temp[1]
            go=0
    return go
def search_4(now):
    global result
    if(maze[now[0], now[1]-1]==0 and now[1]-1>=0):
        push([[now[0], now[1]-1], 4)
        now=[now[0], now[1]-1]
        go=1
    else:
        if(now==end):
            result=1
        else:
            temp=pop()
            now=temp[0]
            direction=temp[1]
            go=0
    return go
def iteration
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
    s=[]
    while(result!=1 and count<2):
        if(search_1(now))
