N=int(input())
rope=[]
for i in range(N):
    rope.append(int(input()))
weight=0
count=1
rope.sort(reverse=True)
for i in range(N):
    minimum=rope[count-1]
    temp=minimum*count
    if(temp>weight):
        weight=temp
    count+=1
print(weight)