T=int(input())
for test_case in range(1, T+1):
    P, Q, R, S, W=map(int, input().split())
    A=W*P
    if(W<=R):
        B=Q
    else:
        B=Q+S*(W-R)
    if(A<B):
        print("#{0} {1}".format(test_case, A))
    else:
        print("#{0} {1}".format(test_case, B))