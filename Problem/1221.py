T=int(input())
for test_case in range(1, T+1):
    case, N=input().split()
    N=int(N)
    num_sequence=list(input().split())
    char=['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count=[]
    for i in range(10):
        count.append(num_sequence.count(char[i]))
    result=[]
    for i in range(10):
        for j in range(count[i]):
            result.append(char[i])
    result=' '.join(result)
    print("{0} {1}".format(case, result))