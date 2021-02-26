def dfs(x, y):
    global matrix, visited


T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1
     

# 푸는중


