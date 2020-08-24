def get_power_set(s):
    power_set=[[]]
    for elem in s:
        for sub_set in power_set:
            power_set=power_set+[list(sub_set)+[elem]]
    return power_set

A=[1,2,3,4,5,6,7,8,9,10,11,12]
power_set=get_power_set(A)
T=int(input())
for test_case in range(1, T+1):
    count=0
    NK=input().split()
    for i in range(len(NK)):
        NK[i]=int(NK[i])
    for i in range(len(power_set)):
        if(len(power_set[i])==NK[0]):
            sum=0
            for j in range(len(power_set[i])):
                sum+=power_set[i][j]
            if(sum==NK[1]):
                count+=1
    print("#{0} {1}".format(test_case, count))

