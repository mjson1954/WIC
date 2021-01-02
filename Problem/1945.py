T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    num=[11,7,5,3,2]
    result=[0 for i in range(5)]
    for i in range(len(num)):
        while(N%num[i]==0):
            result[i]+=1
            N=N//num[i]
    result=map(str, result)
    result=" ".join(result)
    print("#{0} {1}".format(test_case, result[::-1]))