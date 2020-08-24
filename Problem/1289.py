T=int(input())
for test_case in range(1, T+1):
    memory=input()
    count=0
    now='0'
    for i in range(len(memory)):
        if(memory[i]!=now):
            count+=1
            now=memory[i]
    print("#{0} {1}".format(test_case, count))