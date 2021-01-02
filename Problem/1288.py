T=int(input())
for test_case in range(1, T+1):
    num=[0 for i in range(10)]
    count=0
    N=int(input())
    while(0 in num):
        count+=1
        tmp=str(N*count)
        for i in range(len(tmp)):
            num[int(tmp[i])]=1
    print("#{0} {1}".format(test_case, count*N))