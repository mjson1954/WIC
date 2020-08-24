A, B=input().split()
difflist=[]
for i in range(len(B)-len(A)+1):
    temp=0
    for j in range(len(A)):
        if(A[j]!=B[j+i]):
            temp+=1
    difflist.append(temp)
print(min(difflist))