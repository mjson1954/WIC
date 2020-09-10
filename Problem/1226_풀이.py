for tc in range(10):
    N=int(input())
    miro=[list(map(int,input())) for _ in range(16)]
 
    x=1
    y=1
 
    # 오왼하상
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
 
    position=[(y,x)]
    visit=[]
    ans=0
    while position:
        b,a=position.pop()
        if miro[a][b]==3:
            ans=1
        visit.append((b,a))
 
        for j in range(4):
            nx=a+dx[j]
            ny=b+dy[j]
            if (miro[ny][nx]==0 or miro[ny][nx]==3) and (ny, nx) not in visit:
                position.append((ny,nx))
 
    print("#{} {}".format(tc+1,ans))