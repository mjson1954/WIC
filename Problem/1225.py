for test_case in range(1, 11):
    N=int(input())
    integer=list(input().split())
    pos=1
    while(1):
        for i in range(5):
            tmp=int(integer[0])-(i+1)
            result=integer[1:]
            result.append(str(tmp))
            integer=result
            if(tmp<=0):
                integer[-1]='0'
                pos=0
                break
        if(pos==0):
            break
    result=' '.join(result)
    print("#{0} {1}".format(test_case, result))