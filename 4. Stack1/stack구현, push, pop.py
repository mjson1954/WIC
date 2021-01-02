def push(item):
    s.append(item)

def pop():
    if len(s)==0:
        #underflow
        return
    else:
        return s.pop(-1) #마지막 위치의 값 삭제 and return

s=[]
push(1)
push(2)
push(3)
print("pop item =>", pop())
print("pop item =>", pop())
print("pop item =>", pop())
    
