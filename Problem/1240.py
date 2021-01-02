def check(num):
    temp1=(num[0]+num[2]+num[4]+num[6])*3
    temp2=num[1]+num[3]+num[5]
    if((temp1+temp2+num[7])%10==0):
        return sum(num)
    else:
        return 0

T=int(input())
codelist=['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for test_case in range(1, T+1):
    N, M=map(int, input().split())
    entire=[]
    for i in range(N):
        string=input()
        entire.append(string)
        if('1' in string):
            code=string
    start=-1
    end=-1
    # print("code")
    # print(code)
    for i in range(M//2):
        if(code[i]=='1' and start==-1):
            start=i
        if(code[M-1-i]=='1' and end==-1):
            end=M-i-1
        if(start!=-1 and end!=-1):
            break
    # print(start, end)
    # startgap=start
    # endgap=M-1-end
    # print(code[start:end+1]) #1시작1끝
    # print(len(code[start:end+1]))
    # print(startgap, endgap)
    if(len(code[start:end+1])==56):
        code=code[start:end+1]
    else:
        gap=56-len(code[start:end+1])
        for i in range(gap+1):
            zero=[i, gap-i] #left, right
            # print(zero)
            templeft='0'*zero[0]
            tempright='0'*zero[1]
            tempcode=templeft+code[start:end+1]+tempright
            pos=1
            for j in range(8):
                if(tempcode[j*7:(j+1)*7] not in codelist):
                    pos=0
                    break
            if(pos==1):
                code=tempcode
                break
    # print("최종", code)
    num=[]
    for i in range(8):
        numcode=code[i*7:(i+1)*7]
        # print(numcode)
        for j in range(10):
            if(codelist[j]==numcode):
                num.append(j)
                break
    # print(num)
    print("#{0} {1}".format(test_case, check(num)))

        

            


        

