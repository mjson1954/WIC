T=int(input())
for test_case in range(1, T+1):
    TC=int(input())
    score=list(map(int, input().split()))
    scoreList=[0]*101
    for i in range(len(score)):
        scoreList[score[i]]+=1

    m=max(scoreList)
    freq=[i for i,j in enumerate(scoreList) if j==m]
    print("#{0} {1}".format(test_case, max(freq)))
    