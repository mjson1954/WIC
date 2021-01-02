T = int(input())
def is_there(list, x):
    for i in range(len(list)):
        if(x==list[i]):
            return 1
    return 0

def check(KNM, charge_location, x,result,count):
    while(KNM[0]-count>0):
        if(is_there(charge_location, x+KNM[0]-count)):
            result+=1
            #print(x+KNM[0]-count)
            x+=KNM[0]-count
            if(x>=KNM[1]):
                return result
            count=0
            check(KNM, charge_location, x, result, count)
        else:
            count+=1
            check(KNM, charge_location, x, result, count)
    if(count>KNM[0]):
        return 0
    return result
            
for test_case in range(1, T + 1):
    tmp=input()
    KNM=[]
    KNM=tmp.split(' ')
    for i in range(3):
        KNM[i]=int(KNM[i])
    charge_location=[]
    tmp=input()
    charge_location=tmp.split(' ')
    for i in range(len(charge_location)):
        charge_location[i]=int(charge_location[i])

    print(check(KNM, charge_location, 0, 0, 0))
    
    
