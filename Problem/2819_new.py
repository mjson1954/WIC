def dfs(i, j):
    global board
    start=board[i][j]
    string=[]
    temp=[]
    for x in range(j+1, 4):
        temp.append(board[i][x])
    if(len(temp)!=0):
        string.append(temp)
    temp=[]
    for x in range(0, j):
        temp.append(board[i][x])
    if(len(temp)!=0):
        string.append(temp)
    temp=[]
    for x in range(i+1, 4):
        temp.append(board[x][j])
    if(len(temp)!=0):
        string.append(temp)
    temp=[]
    for x in range(0, i):
        temp.append(board[x][j])
    if(len(temp)!=0):
        string.append(temp)
    print(string)
    result=start
    for i in range(len(string)):
        result=result+''.join(string[i])
    print(result)

    
    # tempj=j
    # tempi=i
    # while(tempj<3):
    #     tempj+=1

    #     string=string+board[i][tempj]
    # tempj=j
    # while(tempj>0):
    #     tempj-=1
    #     string=string+board[i][tempj]
    # while(tempi>0):
    #     tempi-=1
    #     string=string+board[tempi][j]
    # tempi=i
    # while(tempi<3):
    #     tempi+=1
    #     string=string+board[tempi][j]
    # print(string)
    


T=int(input())
for test_case in range(1, T+1):
    board=[]
    result=[]
    for _ in range(4):
        board.append(list(input().split()))
    for i in range(4):
        for j in range(4):
            dfs(i,j)
