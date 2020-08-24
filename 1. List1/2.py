T=int(input())
for test_case in range(1, T+1):
    K, N, M=map(int, input().split())
    busstop=[0 for i in range(N+1)]
    busLocation=0
    chargeCount=0
    posibility=1
    temp=list(map(int, input().split()))
    for i in range(M):
        busstop[temp[i]]=1
    while(busLocation+K<N and posibility==1):
        if(busstop[busLocation+K]==1):
            chargeCount+=1
            busLocation+=K
        else:
            plus=K-1
            while(1):
                if(plus==0):
                    posibility=0
                    break
                if(busstop[busLocation+plus]==1):
                    chargeCount+=1
                    busLocation+=plus
                    break
                else:
                    plus-=1
    if(posibility==1):
        print("#{0} {1}".format(test_case, chargeCount))
    else:
        print("#{0} {1}".format(test_case, "0"))