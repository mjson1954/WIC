T=int(input())
def insert(alphabet, count):
    x=0
    global result
    global idx
    if(idx>=N-1):
        result.append([])
        if(count>10):
            result.append([])
    while(x<count):
        result[idx].append(alphabet)
        x+=1
        if(len(result[idx])==10):
            idx+=1

for test_case in range(1, T+1):
    N=int(input())
    result=[[] for i in range(N)]
    idx=0
    for i in range(N):
        alphabet, count=input().split()
        count=int(count)
        insert(alphabet, count)
    print("#{0}".format(test_case))
    for i in range(len(result)):
        joined="".join(result[i])
        print(joined)