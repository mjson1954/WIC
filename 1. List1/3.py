T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    count=[0 for _ in range(10)]
    num=input()
    for j in range(len(num)):
        count[int(num[j])]+=1
    max_value=max(count)
    for j in range(len(count)):
        if(count[j]==max_value):
            max_index=j
    print("#{0} {1} {2}".format(test_case, max_index, max_value))

