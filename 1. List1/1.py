S=int(input())
result=[]
for i in range (1,S+1):
	a=[]
	T=int(input())
	num=input()
	a=num.split(' ')
	for j in range(len(a)):
		a[j]=int(a[j])
	temp=max(a)-min(a)
	result.append(temp)
	print("#",i, result)
        del result[0]
        
