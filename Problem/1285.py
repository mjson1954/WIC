T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    location=list(map(int, input().split()))
    min=100000
    count=0
    for i in range(N):
        if(location[i]<0):
            location[i] = -location[i]

        if(min>location[i]):
            min=location[i]
            count=1
        elif(min==location[i]):
            count+=1
        else:
            pass
    print("#{0} {1} {2}".format(test_case, min, count))