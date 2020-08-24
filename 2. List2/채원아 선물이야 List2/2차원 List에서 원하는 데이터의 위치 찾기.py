n,m=map(int, input().split())

#1
newlist=[]
mylist=[0 for _ in range(n)]
for i in range(n):
    mylist[i]=list(map(int, input().split()))
    for j in range(m):
        if mylist[i][j]==1:
            newlist.append([i,j])

#2
mylist=[list(map(int, input().split())) for _ in range(n)]
newlist=[(i,j) for i in range(n) for j in range(m) if mylist[i][j]==1]


