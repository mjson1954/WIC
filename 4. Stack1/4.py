T=int(input())
def equaltest(s):
    count=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1
            break
    if(count>0):
        return i
    else:
        return -1
    

for test_case in range(1, T+1):
    text=input()
    s=[]
    new=[]
    for i in range(len(text)):
        s.append(text[i])
    while(equaltest(s)>-1):
        i=equaltest(s)
        for j in range(0, i):
            new.append(s[j])
        for j in range(i+2, len(s)):
            new.append(s[j])
        s=new
        new=[]

    print("#{0} {1}".format(test_case, len(s)))
