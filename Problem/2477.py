T = int(input()) # 총 테스트 케이스 개수

for test_case in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    # N: 접수 창구 개수, M: 정비 창구 개수
    # K: 방문한 고객 수, A: 이용한 접수 창구번호, B: 이용한 정비 창구번호
    reception = list(map(int, input().split())) # 접수 창구가 걸리는 시간
    repair = list(map(int, input().split())) # 정비 창구가 걸리는 시간
    person = list(map(int, input().split())) # K명의 고객이 도착하는 시간
    
    visit = [0] * K 
    reception_visit = [0] * N
    repair_visit = [0] * M

    waiting = []
    repair_waiting = []

    time = 0

    track = {x:[] for x in range(K)}

    while sum([len(x) for x in track.values()]) < 2 * K: # 각 고객의 접수창구, 정비창구 방문 기록이 2번씩 되면 while문 break
        for i in range(K):
            if not visit[i] and person[i] == time: # 방문 아직 안했는데 지금 방문할 시간이라면
                waiting.append(i) # 일단 대기에 넣기
                visit[i] = 1 # 방문했다

        if waiting: 
            cnt = 0 
            for p in waiting:
                for i in range(N): # 모든 접수 창구에 대해
                    if not reception_visit[i]: # 접수 창구가 비어있다면
                        reception_visit[i] = (p, time + reception[i]) 
                        track[p].append(i) # 접수 창구 번호 넣기
                        cnt += 1
                        break
            for _ in range(cnt): waiting.pop(0) # 대기열에서 빼기
        
        for i in range(N): # 접수 끝내고 대기 장소에 넣기
            if reception_visit[i] != 0  and reception_visit[i][1] == time: # 접수창구가 비어있지 않고, 나갈 사람이면
                repair_waiting.append(reception_visit[i][0]) # 수리 대기열에 넣기
                reception_visit[i] = 0 # 접수 창구 비우기

        if repair_waiting:
            cnt = 0
            for p in repair_waiting: 
                for i in range(M): # 모든 수리 창구에 대해
                    if not repair_visit[i]: # 수리 창구가 비어있으면
                        repair_visit[i] = (p, time + repair[i]) 
                        track[p].append(i) # 수리 창구 번호 넣기
                        cnt += 1
                        break
            for _ in range(cnt): repair_waiting.pop(0) # 대기열에서 빼기

        for i in range(M): # 모든 수리 창구에 대해
            if repair_visit[i] != 0 and repair_visit[i][1] == time: # 수리창구가 비지 않았는데 나갈 시간이라면
                repair_visit[i] = 0 # 수리 창구 비우기
                
        time += 1 


    result = 0
    for key, val in track.items():
        if val == [A-1, B-1]:
            result += (key+1)
    if not result: # result 가 0 이면 
        print('#{} -1'.format(test_case))
    else:
        print('#{}'.format(test_case), result)
