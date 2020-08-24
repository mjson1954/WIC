T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    distance=0
    velocity=0
    for i in range(N):
        temp=input()
        if(len(temp)==1):
            command=0
        else:
            command, x=map(int, temp.split())
        if(command==1):
            velocity+=x
        elif(command==2):
            velocity-=x
            if(velocity<0):
                velocity=0
        else:
            pass
        distance+=velocity
    print("#{0} {1}".format(test_case, distance))
        