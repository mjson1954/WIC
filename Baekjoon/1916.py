N=int(input()) # 도시의 개수
M=int(input()) # 버스의 개수
W=[[1000000 for i in range(N+1)] for i in range(N+1)]
for i in range(M):
    start, end, weight=map(int, input().split())
    if(W[start][end]==-1):
        W[start][end]=weight
    else:
        if(W[start][end]>weight):
            W[start][end]=weight # 버스 비용 저장
touch=[0 for i in range(N+1)]
length=[0 for i in range(N+1)]
start, end=map(int, input().split())
def dijkstra(n, W):
    global touch
    global length
    for i in range(2, n+1): # 초기화
        touch[i]=start # 초기에는 Y에 노드가 v1밖에 없음
        if(W[start][i]!=-1):
            length[i]=W[start][i] # (v1, vi)의 가중치로 초기화
        else:
            length[i]=100001
    for i in range(n-2): # n-1개의 정점을 Y에 차례로 추가한다
        min=100000
        for j in range(2, n+1):
            if(0<=length[j] and length[j]<min):
                min=length[j]
                vnear=j
        for j in range(2, n+1):
            if(W[vnear][j]!=1000000 and length[vnear]+W[vnear][j]<length[j]):
                length[j]=length[vnear]+W[vnear][j] # Y에 속하지 않는
                touch[j]=vnear # 각 노드에 대해 length[j]를 갱신한다.
        length[vnear]=-1 # vnear가 인덱스인 노드를 Y에 추가한다.
dijkstra(N, W)
result=0
while(1):
    if(touch[end]==start):
        result+=W[start][end]
        break
    else:
        result+=W[touch[end]][end]
        end=touch[end]
print(result)