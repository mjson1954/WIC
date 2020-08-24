T=int(input())
def push(item):
    s.append(item)
def pop():
    if len(s)==0:
        return
    else:
        return s.pop(-1)

for test_case in range(1, T+1):
    s=[]
    text=input()
    result=1
    for i in range(len(text)):
        if(text[i]=="{" or text[i]=="("):
            push(text[i])
        elif(text[i]=="}" or text[i]==")"):
            temp=pop()
            if(temp==None):
                result=0
            if(text[i]=="}" and temp=="("):
                result=0
            elif(text[i]==")" and temp=="{"):
                result=0
    if(len(s)!=0):
        result=0
    
    print("#{0} {1}".format(test_case, result))
