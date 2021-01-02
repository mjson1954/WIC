def binarySearch(end, key):
    count=1
    start=1
    while(start<end):
        middle=(start+end)//2
        if(key==middle):
            return count 
        elif(key<middle):
            count+=1
            end=middle
        else:
            count+=1
            start=middle
    return count

T=int(input())
for test_case in range(1, T+1):
    P, A, B=map(int, input().split())
    count_A=binarySearch(P, A)
    count_B=binarySearch(P, B)
    if(count_A<count_B):
        print("#{0} A".format(test_case))
    elif(count_A>count_B):
        print("#{0} B".format(test_case))
    else:
        print("#{0} 0".format(test_case))
