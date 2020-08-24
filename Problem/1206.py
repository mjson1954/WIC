for test_case in range(1, 11):
    length=int(input())
    height=list(map(int, input().split()))
    sum=0
    for i in range(2, len(height)-2):
        nearby=[height[i-2], height[i-1], height[i+1], height[i+2]]
        if(max(nearby)<height[i]):
            sum+=height[i]-max(nearby)

    print("#{0} {1}".format(test_case, sum))