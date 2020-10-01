n, m = map(int, input().split())
hear = []
hearandsee = []

for i in range(n+m):
    hear.append(input())
hear = sorted(hear)

flag = 0
for i in range(n+m-1):
    if(flag == 1):
        flag = 0
        continue
    if(hear[i] == hear[i+1]):
        hearandsee.append(hear[i])
        flag = 1
     
print(len(hearandsee))
for i in range(len(hearandsee)):
    print(hearandsee[i])