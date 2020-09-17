from collections import deque

INF = 99999
move = [[0, 1], [1, 0], [-1, 0], [0, -1]] # 우, 하, 좌, 상

def solution(queue):
    while(len(queue)): # 큐가 빌때까지
        x, y = queue.popleft() 
        for i in range(len(move)):
            dx, dy = x+move[i][0], y+move[i][1] # 새로운 경로
            if(0 <= dx < N and 0 <= dy < N): # 유효한 경로인지 검사
                if(distance[dx][dy] > distance[x][y] + road[dx][dy]): 
                    distance[dx][dy] = distance[x][y] + road[dx][dy] # 최소거리 갱신
                    queue.append((dx, dy))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = []
    for i in range(N):
        road.append(list(map(int, input())))
    distance = [[INF for _ in range(N)] for _ in range(N)] # 특정 좌표까지 가기 위한 최소 거리
    distance[0][0] = 0
    queue = deque()
    queue.append((0, 0))
    solution(queue)
    print("#{0} {1}".format(tc, distance[N-1][N-1]))