import math
Count=0
def findRoot(num, count):
    global Count
    while(count!=Count):
        root=math.ceil((num-1)/2)+1
        Count+=1
        

    return root

T=int(input())
for test_case in range(1, T+1):
    num=int(input())
    print(findRoot(num,2))
    num2=num//2
   
