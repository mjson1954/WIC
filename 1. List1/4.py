T = int(input())
for test_case in range(1, T + 1):
    tmp=input()
    NM=[]
    NM=tmp.split(' ')
    for j in range(len(NM)):
        NM[j]=int(NM[j])                
    num=input()
    a=[]
    a=num.split(' ')
    for j in range(NM[0]):
        a[j]=int(a[j])
    print(a)
    sum=[]
    for i in range(NM[0]-NM[1]+1):
        tempsum=0
        for s in range(NM[1]):
            tempsum=tempsum+a[i+s]
        sum.append(tempsum)
    print(sum)
    result=max(sum)-min(sum)
    print(result)
