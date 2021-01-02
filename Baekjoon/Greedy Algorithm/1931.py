N=int(input())
meetingInfo=[]
time=[]
for i in range(N):
    start, end=map(int, input().split())
    meetingInfo.append((start, end))
meetingInfo.sort(key=lambda element:element[1])
print(meetingInfo)
meetingPlan=[]
x=0
for i in range(len(meetingInfo)):
    #print("x: ",x)
    if(i>0 and meetingInfo[i][0]<x):
        continue
    start=meetingInfo[i][0]
    end=meetingInfo[i][1]
    #print("처음", start, end)
    for j in range(i, len(meetingInfo)):
        if(meetingInfo[j][1]<=end and meetingInfo[j][0]>=start):
            start=meetingInfo[j][0]
            end=meetingInfo[j][1]
            #print(start, end)
        else:
            break
    meetingPlan.append((start, end))
    x=end


print(meetingPlan)
    
