for test_case in range(1, 11):
    N=int(input())
    crypto=list(input().split())
    command_N=int(input())
    command=list(input().split())
    for i in range(len(command)):
        if(command[i]=='I'):
            x=int(command[i+1])
            y=int(command[i+2])
            for j in range(y):
                s=command[i+3+j]
                crypto.insert(x+j, s)
            # i+=2+y
        else:
            pass
    result=' '.join(crypto[:10])
    print("#{0} {1}".format(test_case, result))