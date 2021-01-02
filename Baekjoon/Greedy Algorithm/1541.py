exp=list(input().split('-'))
minsum=0
for i in range(len(exp)):
    if('+' in exp[i]):
        tmp=list(exp[i].split('+'))
        sum=0
        for j in range(len(tmp)):
            sum+=int(tmp[j])
        exp[i]=sum
    else:
        pass
exp=list(map(int, exp))
for i in range(len(exp)):
    if(i==0):
        minsum=exp[i]
    else:
        minsum-=exp[i]
print(minsum)