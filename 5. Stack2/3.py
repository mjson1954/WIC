def push(item, s):
    s.append(item)

def pop(s):
    if len(s)==0:
        #underflow
        return
    else:
        return s.pop(-1) #마지막 위치의 값 삭제 and return
T=int(input())
def partition(j, card, result):
    left=card[0:j]
    right=card[j+1:]
    result.append(left)
    result.append(right)
        
for test_case in range(1,T+1):
    num=int(input())
    card=list(map(int, input().split()))
    stack=[]
    j_location=[]
    j=num
    while(j>3):
        j=(j+1)//2
        j_location.append(j)
    print(j_location)
    print(card)
    result=[]
    count=0
    while(count<len(j_location)):
        partition(j_location[i], card, result)
        count+=1
        if(result[0]>3):
            partition(j_location[i+1], result[0], result[0])
            count+=1
        elif(result[1]>3):
            partition(j_location[i+1], result[1], result[1])
            count+=1
            
    
