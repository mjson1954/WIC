def dfs(matrix, start, end):
    visited = [[0 for _ in range(16)] for _ in range(16)]
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 우, 하, 좌, 상
    location = start # 시작점은 출발점
    trace = [start] # 경로
    result = -1 # 최종 결과 (0: 경로없음, 1: 경로있음)

    while(result == -1): # 어떠한 결과가 나오면 중지
        break_the_move = 0
        break_the_move_2 = 0
        break_pop = 0
        for i in range(len(move)): # 어느 방향으로 움직일지 찾기
            idx = [location[0] + move[i][0], location[1] + move[i][1]] 
            if(idx == end): # 도착점이면 
                result = 1 # 경로있다!!
            if(visited[idx[0]][idx[1]] == 0 and matrix[idx[0]][idx[1]] == '0'):
                visited[idx[0]][idx[1]] = 1 # 방문
                location = idx # 이동
                trace.append(idx) # 경로에 넣기
                break_the_move = 1 
            if(break_the_move == 1): # 이동했으니까 방향 탐색 중지
                break
        
        if(break_the_move == 0): # 이동을 못했어!!!
            while(break_pop == 0):
                if(len(trace) == 0): # 더이상 pop할 trace가 없으면 최종 경로가 없는것
                    result = 0
                    break
                pre = trace.pop()
                location = pre # 이전 위치로 이동
                for i in range(len(move)): # 이전 위치에서 새롭게 갈데있나?
                    idx = [location[0]+move[i][0], location[1]+move[i][1]]
                    if(visited[idx[0]][idx[1]] == 0 and matrix[idx[0]][idx[1]] == '0'):
                        # 오키 새롭게 갈데 찾았따!
                        break_pop = 1 # 경로 pop 중지
                        trace.append(idx)
                        break_the_move_2 = 1 
                    if(break_the_move_2 == 1): # 방향 탐색 중지
                        break
                
    return result
    
for test_case in range(1, 11):
    tc = input()
    matrix = []
    for i in range(16):
        temp = list(input())
        if('2' in temp): # 시작점 찾기
            start = [i, temp.index('2')]
        elif('3' in temp): # 끝나는점 찾기
            end = [i, temp.index('3')]
        else:
            pass
        matrix.append(temp)
    # print(start, end)
    print("#{0} {1}".format(test_case, dfs(matrix, start, end)))