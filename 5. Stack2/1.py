T=int(input())
def push(item):
    s.append(item)
def pop():
    if len(s)<0:
        #underflow
        return 'error'
    else:
        return s.pop(-1) #마지막 위치의 값 삭제 and return
for test_case in range(1, T+1):
    line=list(input().split())
    s=[]
    operator=['+','-','*','/']
    for i in range(len(line)):
        if(line[i]=='.'):
            if(len(s)==1):
                print("#{0} {1}".format(test_case, pop()))
            else:
            	print("#{0} {1}".format(test_case, "error"))
        elif(line[i] in operator):
            if(len(s)<2):
                print("#{0} {1}".format(test_case, "error"))
                break
            if(line[i]=='+'):
                temp=pop()+pop()
                push(temp)
            elif(line[i]=='-'):
                b=pop()
                a=pop()
                temp=a-b
                push(temp)
            elif(line[i]=='*'):
                temp=pop()*pop()
                push(temp)
            elif(line[i]=='/'):
                b=pop()
                a=pop()
                if(b==0):
                    print("#{0} {1}".format(test_case, "error"))
                    break
                temp=a//b
                push(temp)
        else:
            push(int(line[i]))

        
    
            
    
