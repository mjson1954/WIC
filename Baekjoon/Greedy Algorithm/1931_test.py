N=int(input())
meetingInfo=[]
time=[]
for _ in range(N):
    start, end=map(int, input().split())
    meetingInfo.append((start, end))
meetingInfo.sort(key=lambda element:element[1])
print(meetingInfo)
meetingPlan=[]
i=len(meetingInfo)-1
for s in range(len(meetingInfo)):
    if(s>0 and meetingInfo[i][1]>=x):
        i-=1
        continue
    start=meetingInfo[i][0]
    end=meetingInfo[i][1]
    print(start, end)
    j=i-1
    for _ in range(len(meetingInfo)-1):
        if(meetingInfo[j][1]==end and meetingInfo[j][0]>start):
            start=meetingInfo[j][0]
            end=meetingInfo[j][1]
        else:
            j-=1
    meetingPlan.append((start,end))
    x=start
    i-=1

    

print(meetingPlan)
    
