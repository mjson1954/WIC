def select(list, k):
    for i in range(0, k):
        minIndex=i
        for j in range(i+1, len(list)):
            if list[minIndex]>list[j]:
                minIndex=j
        list[i], list[minIndex]=list[minIndex], list[i]
    return list[k-1]

T=int(input())
for test_case in range(1, T+1):
    result=[]
    N=int(input())
    num=input().split()
    for i in range (len(num)):
        num[i]=int(num[i])
    result.append(select(num,len(num)))
    result.append(select(num,1))
    result.append(select(num,len(num)-1))
    result.append(select(num,2))
    result.append(select(num,len(num)-2))
    result.append(select(num,3))
    result.append(select(num,len(num)-3))
    result.append(select(num,4))
    result.append(select(num,len(num)-4))
    result.append(select(num,5))
    print("#{0}".format(test_case), end=' ')
    for i in range (10):
        print(result[i], end=' ')
    print(' ')
