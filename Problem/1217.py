def involution(N, M):
    global result
    if(M==0):
        return
    else:
        result=result*N
        involution(N, M-1)
for test_case in range(1, 11):
    T=int(input())
    N, M=map(int, input().split())
    result=1
    involution(N, M)
    print("#{0} {1}".format(test_case, result))