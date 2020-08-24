T=int(input())
def fact(x):
    result=1
    while(x>0):
        result=result*x
        x-=1
    return result

for test_case in range(1, T+1):
    num=int(input())
    n=num//10
    count=n//2
    result=0
    for i in range(1, count+1):
        temp=n-i
        result+=fact(temp)/(fact(temp-i)*fact(i))*pow(2,i)
    result+=1
    print("#{0} {1}".format(test_case, int(result)))
    
    
