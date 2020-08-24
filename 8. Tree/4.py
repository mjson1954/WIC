T=int(input())
for test_case in range(1, T+1):
    N, M, L=map(int, input().split())
    tree=[0]*(N+1)
    for i in range(M):
        location, num=map(int, input().split())
        tree[location]=num
    empty=[]
    for i in range(1, N+1):
        if(tree[i]==0):
            empty.append(i)
    empty.sort(reverse=True)
    for i in range(len(empty)):
        idx=empty[i]
        if(2*idx<=N and 2*idx+1<=N):
            tree[idx]=tree[idx*2]+tree[idx*2+1]
        elif(2*idx<=N and 2*idx+1>N):
            tree[idx]=tree[idx*2]
        else:
            continue
    print("#{0} {1}".format(test_case, tree[L]))
        
        