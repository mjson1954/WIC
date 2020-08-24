T=int(input())
def BMalgorithm(p, t,i,j, skip,count, x):
    while(i<=j and j<len(t)):
        if(p[x]!=t[j]):
            s=0
            while(s<len(p)):
                if(t[j]==p[s]):
                    j=j+skip[s+1]
                    break
                else:
                    s+=1
            if(s==len(p)):
                j=j+skip[0]
            i=j-len(p)+1 
            count=0 
            x=len(p)-1 
            BMalgorithm(p, t, i, j, skip,count,x)
        else:
            count+=1
            if(count==len(p)):
                return 1
            j=j-1
            x=x-1
            BMalgorithm(p, t, i, j, skip,count,x)
    return 0
    
    
        
for test_case in range(1, T+1):
    pattern=list(input())
    text=list(input())
    skip=[]
    for i in range(len(pattern)+1):
        skip.append(len(pattern)-i)
    print("#{0} {1}".format(test_case, BMalgorithm(pattern, text, 0, len(pattern)-1, skip, 0, len(pattern)-1)))
    
