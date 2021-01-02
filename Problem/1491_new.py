import math
def get_factors(n):
    factors=[]
    for i in range(1, n+1):
        if(n%i==0):
            factors.append(i)
    return factors
def get_num(n):
    temp=math.floor(math.sqrt(n))
    return temp

T=int(input())
for test_case in range(1, T+1):
    N, A, B=map(int, input().split())
    factors=get_factors(N)
    print(factors)
    minimum=0
    N_temp=N
    exp_2=0
    R=get_num(N)
    C=get_num(N)
    exp_1=A*(R-C)+B*(N-R*C)

    while(1):
        if(len(factors)%2!=0):
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
    print("#{0} {1}".format(test_case, min(exp_1, exp_2)))