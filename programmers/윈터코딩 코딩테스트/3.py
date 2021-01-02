
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
v= [[0,0,1],[2,2,1],[0,0,0]]
def bfs(x, y, num, v):
    n = len(v)
    m = len(v[0])
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and v[q][w] == num:
                v[q][w] = -1
                queue.append([q, w])

def solution(v):
    n = len(v)
    m = len(v[0])
    answer = [0 for _ in range(3)]
    for q in range(n):
        for w in range(m):
            if(v[q][w] == -1):
                continue
            if(v[q][w] == 1):
                bfs(q, w, 1, v)
                v[q][w] = -1
                answer[1] += 1
            elif(v[q][w] == 0):
                bfs(q, w, 0, v)
                v[q][w] = -1
                answer[0] += 1
            else:
                bfs(q, w, 2, v)
                v[q][w] = -1
                answer[2] += 1
                    
    return answer



print(solution(v))
