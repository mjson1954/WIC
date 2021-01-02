T=int(input())
for test_case in range(1, T+1):
    N, M, L=map(int, input().split())
    sequence=list(map(int, input().split()))
    for i in range(M):
        index_location, index_value=map(int, input().split())
        temp=sequence[index_location:]
        sequence[index_location]=index_value
        result=sequence[:index_location+1]
        result.extend(temp)
        sequence=result
    print("#{0} {1}".format(test_case, sequence[L]))


