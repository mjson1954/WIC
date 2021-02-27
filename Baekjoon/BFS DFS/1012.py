dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
temp_answer = 0

def dfs(a, b, m, n):
    global matrix, visited, temp_answer
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if(0<=x<n and 0<=y<m):
            if(visited[x][y]==0 and matrix[x][y]==1):
                visited[x][y] = 1
                temp_answer += 1
                dfs(x, y, m, n)

T = int(input())
for tc in range(T):
    answer = 1
    m, n, k = map(int, input().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    for i in range(n):
        for j in range(m):
            if(visited[i][j]==0 and matrix[i][j]==1):
                dfs(i, j, m, n)
                if(temp_answer > 0):
                    answer += 1
                    temp_answer = 0
    print(answer)
     
# 푸는중


