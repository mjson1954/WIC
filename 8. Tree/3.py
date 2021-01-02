T=int(input())
for test_case in range(1, T+1):
    nodeNum=int(input())
    tree=[0]
    nodeSeq=list(map(int, input().split()))
    for i in range(nodeNum):
        tree.append(nodeSeq[i])
        idx=i+1
        while(tree[idx//2]>tree[idx] and idx>=2):
            tmp=tree[idx//2]
            tree[idx//2]=tree[idx]
            tree[idx]=tmp
            idx=idx//2
    sum=0
    idx=nodeNum//2
    while(idx>=1):
        sum+=tree[idx]
        idx=idx//2
    print("#{0} {1}".format(test_case, sum))
