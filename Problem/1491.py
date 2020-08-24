def get_factors(n):
    factors=[]
    for i in range(1, n+1):
        if(n%i==0):
            factors.append(i)
    return factors

T=int(input())
for test_case in range(1, T+1):
    N, A, B=map(int, input().split())
    factors=get_factors(N)
    print(factors)
    minimum=0
    N_temp=N
    exp_1=0
    exp_2=0
    while(exp_1==0):
        if(len(factors)%2!=0):
            idx=(len(factors)-1)//2
            R=factors[idx]
            C=factors[idx]
            exp_1=A*(R-C)+B*(N-R*C)
            break
        else:
            right_idx=len(factors)//2
            left_idx=right_idx-1
            R=factors[right_idx]
            C=factors[left_idx]
            temp=A*(R-C)+B*(N-R*C)
            if(minimum==0):
                minimum=temp
                N_temp-=1
                factors=get_factors(N_temp)
                continue
            if(temp<=minimum):
                minimum=temp
            else:
                exp_2=minimum
            N_temp-=1
            factors=get_factors(N_temp)
    print(exp_1, exp_2)
    if(exp_1<exp_2):
        exp=exp_1
    else:
        exp=exp_2
    print("#{0} {1}".format(test_case, exp))