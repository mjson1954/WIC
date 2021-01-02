T=int(input())
for test_case in range(1, T+1):
    N, M=map(int, input().split())
    result=list(map(int, input().split()))
    for i in range(M-1):
        plus=list(map(int, input().split()))
        if(max(result)<=plus[0]):
            result.extend(plus)
            continue
        for j in range(len(result)):
            if(result[j]>plus[0]):
                temp=result[:j] 
                temp.extend(plus)
                temp.extend(result[j:])
                result=temp
                break
    reverse_list=result[::-1]
    topTen=list(map(str, reverse_list[:10]))
    print("#{0} {1}".format(test_case, ' '.join(topTen)))