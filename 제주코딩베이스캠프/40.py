limit = int(input())
n = int(input())
weightsum = 0
result = -1
for i in range(n):
    weight = int(input())
    weightsum += weight
    if(weightsum > limit and result == -1):
        result = i
        
print(result)

