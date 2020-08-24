T=int(input())
def check(x, y):
    global result
    global dic
    if(y in dic[x]):
        result=1
    else:
        temp=dic[x]
        if(len(temp)==0):
            result=0
        else:
            for i in range(len(temp)):
                if(result==1):
                    break
                else:
                    check(temp[i], y)
    return result

for test_case in range(1, T+1):
    result=0
    V, E=map(int, input().split())
    dic={}
    for i in range(1, V+1):
        dic[i]=[]
    for i in range(E):
        v, w=map(int, input().split())
        dic[v].append(w)
    print(dic)
    x, y=map(int, input().split())
    print("#{0} {1}".format(test_case, check(x, y)))