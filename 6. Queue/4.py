def bfs(queue):
    global n
    if S==G:
        return
    while queue:
        size = len(queue)
        n+=1
        for i in range(size):
            tem = queue.pop(0)
            for j in con[tem]:
                if visit[j]==1:
                    continue
                visit[j] = 1
                queue.append(j)
        if G in queue:
            return
    n=0

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    con = [[] for i in range(V + 1)] 
    visit = [0] * (V + 1)       
    for i in range(E):   
        x, y = map(int, input().split())
        con[x].append(y)
        con[y].append(x)
    S, G = map(int, input().split())
    queue = [S]   
    visit[S] =1 
    n = 0
    bfs(queue)
    print("#{} {}".format(test_case, n))