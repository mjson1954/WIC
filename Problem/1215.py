def check(line, n):
    global count
    for i in range(len(line)):
        first=line[i] # 회문의 첫번째 글자
        index=[j for j,x in enumerate(line) if x==first and j>i]
        for s in range(len(index)):
            temp=line[i:index[s]+1] # 회문 후보(처음과 끝이 같은)
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
            if(pos==1 and len(temp)==n):
                count+=1

for test_case in range(1, 11):
    n=int(input())
    sequence=[]
    sequence_b=[[] for i in range(8)]
    count=0
    for i in range(8):
        temp=list(input())
        sequence.append(temp)
        check(temp, n)

    for i in range(8):
        for j in range(8):
            sequence_b[j].append(sequence[i][j])

    for i in range(8):
        check(sequence_b[i], n)

    print("#{0} {1}".format(test_case, count))

