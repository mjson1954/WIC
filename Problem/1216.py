def check(line):
    global maxlen
    for i in range(len(line)):
        first=line[i] # 회문의 첫번째 글자
        index=[j for j,x in enumerate(line) if x==first and j>i]
        # print(index)
        for s in range(len(index)):
            temp=line[i:index[s]+1] # 회문 후보(처음과 끝이 같은)
            # print("temp: ", temp)
            pos=-1
            t=1
            while(1):
                if(t>=len(temp)//2):
                    pos=1
                    break
                if(temp[t]==temp[-1-t]):
                    t+=1
                else:
                    pos=0
                    break
            # print("pos: ", pos)
            if(pos==1 and maxlen<len(temp)):
                maxlen=len(temp)
            # print("maxlen: ", maxlen)
         
# check('abcacab')

for test_case in range(1, 11):
    T=int(input())
    sequence=[]
    sequence_b=[[] for i in range(100)]
    maxlen=1
    for i in range(100):
        temp=list(input())
        sequence.append(temp)
        check(temp)
    # print(sequence[0])
    for i in range(100):
        for j in range(100):
            sequence_b[j].append(sequence[i][j])
    # print(sequence_b[0])
    for i in range(100):
        check(sequence_b[i])
    print("#{0} {1}".format(test_case, maxlen))





