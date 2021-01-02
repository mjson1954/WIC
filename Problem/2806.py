T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    board=[[0 for i in range(N)] for i in range(N)]
    # print(board)
    pos=[[1 for i in range(N)] for i in range(N)]
    for i in range(N):
        if(i==0 or i==1):
            continue
        for j in range(N):
            pos[0][j]=0 # 첫째줄 제거
            pos[j][i]=0 # 세로 제거
        # print(pos)
        for j in range(N):
            if(i+j<N):
                pos[j][i+j]=0 # 양대각선 제거
            if(j-i>=0):
                pos[j][j-i]=0 # 음대각선 제거
        pos[0][i]=1 # 첫째줄 선택


        print(pos)
        
