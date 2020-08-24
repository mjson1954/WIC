T=int(input())
for test_case in range(1, T+1):
    alpha=input()
    dic={}
    for i in range(len(alpha)):
        if(not(alpha[i] in dic)):
            dic[alpha[i]]=0
    text=input()
    for i in range(len(text)):
        if(text[i] in dic):
            dic[text[i]]+=1
    value=list(dic.values())
    print("#{0} {1}".format(test_case, max(value)))
