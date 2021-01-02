def number_triangle(a, k):
    global best # 각 단계별 최대 합
    global best_sequence # 최대 합 경로
    max_result=0 # 최종 최대 합
    for i in range(1, k+1):
        for j in range(1, i+1):
            if(best[i-1][j-1][0]>=best[i-1][j][0]): # best배열 값을 비교하여
                best[i][j]=(a[i][j]+best[i-1][j-1][0], "L") 
                # 각 단계별 최대 합을 구하고 방향을 저장한다.
            else:
                best[i][j]=(a[i][j]+best[i-1][j][0], "R")
    for i in range(1, k+1):
        if(max_result<best[k][i][0]): # 레벨 k에서 가장 큰 값을 찾는다
            max_result=best[k][i][0] # 최종 최대 합
            idx=i # 최종 최대 합의 열 인덱스
    temp=k-1
    x=k
    for i in range(k):
        if(best[x][idx][1]=="L"): # 왼쪽을 접근해야 할 때
            best_sequence[temp]=best[x][idx][0]-best[x-1][idx-1][0]
            idx-=1
        else: # 오른쪽을 접근해야 할 때
            best_sequence[temp]=best[x][idx][0]-best[x-1][idx][0]
        temp-=1
        x-=1
    return max_result # 최대 합 반환

k=int(input())
a=[[0 for i in range(k+1)]] # 숫자 삼각형 배열
best=[[(0,0) for i in range(k+1)] for i in range(k+1)] # 각 단계별 최대 합
best_sequence=[0 for i in range(k)] # 최대 합 경로
for i in range(k):
    seq=list(map(int, input().split()))
    while(len(seq)<k):
        seq.append(0) # 각 단계의 배열 크기가 K가 되도록 0을 붙여준다.
    seq.insert(0, 0) # 맨 앞에 0을 추가하여 인덱스 1부터 숫자가 저장되게 한다.
    a.append(seq)
print("최대 합:", number_triangle(a, k))
print("최대 합 경로:", best_sequence)

