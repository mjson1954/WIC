T=int(input())   
def right():
    global num, i, j, N
    j+=1
    if(j==N):
        j-=1
        return 0
    if(count[i][j]==0):
        snail[i][j]=num
        count[i][j]=1
        num+=1
        return 1
    else:
        j-=1
        return 0
def left():
    global num, i, j
    j-=1
    if(count[i][j]==0):
        snail[i][j]=num
        count[i][j]=1
        num+=1
        return 1
    else:
        j+=1
        return 0
def up():
    global num, i, j
    i-=1
    if(count[i][j]==0):
        snail[i][j]=num
        count[i][j]=1
        num+=1
        return 1
    else:
        i+=1
        return 0
def down():
    global num, i, j, N
    i+=1
    if(i==N):
        i-=1
        return 0
    if(count[i][j]==0):
        snail[i][j]=num
        count[i][j]=1
        num+=1
        return 1
    else:
        i-=1
        return 0
for test_case in range(1, T+1):
    N=int(input())
    snail=[[0]*N for i in range(N)]
    count=[[0]*N for i in range(N)]
    num=1
    i=0
    j=0
    snail[i][j]=num
    count[i][j]=1
    num+=1
    while(num<=N*N):
        while(1):
            point=right()
            if(point==0):
                break
        while(1):
            point=down()
            if(point==0):
                break
        while(1):
            point=left()
            if(point==0):
                break
        while(1):
            point=up()
            if(point==0):
                break
    print("#{0}".format(test_case))
    for i in range(len(snail)):
        for j in range(len(snail[i])):
            print(snail[i][j], end=' ')
        print()