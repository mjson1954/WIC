n = int(input())
m = int(input())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
visited[0] = 1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

num = 0
def dfs(start):
    global num
    visited[start] = 1
    for i in range(1, n+1):
        if(visited[i]==0 and graph[start][i]==1):
            num += 1
            visited[i] = 1
            dfs(i)
dfs(1)
print(num)
    

