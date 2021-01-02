def newNumber(M, password):
    post=password[M:]
    if(post==[]):
        password.append(password[M-1]+password[0])
        result=password
    else:
        password[M]=password[M-1]+password[M]
        result=password[:M+1]
        result.extend(post)
    return result
    
T=int(input())
for test_case in range(1, T+1):
    m=0
    N, M, K=map(int, input().split())
    password=list(map(int, input().split()))
    for i in range(1, K+1):
        m=m+M
        if(m>len(password)):
            m=m-len(password)
        password=newNumber(m, password)

    reverse_list=password[::-1]
    result=list(map(str, reverse_list[:10]))
    print("#{0} {1}".format(test_case, ' '.join(result)))
    

