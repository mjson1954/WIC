import heapq
import sys
input=sys.stdin.readline

INF=987654321
V, E=map(int, input().split()) # 정점의 수, 간선의 수
k=int(input()) # 시작노드
weight=[INF]*(V+1) # 가중치 배열(INF로 초기화)
heap=[] # 최소 힙
graph=[[] for _ in range(V+1)] # [가중치, 도착노드]가 담긴 배열

for _ in range(E):
    u, v, w=map(int, input().split()) # 출발노드, 도착노드, 가중치
    graph[u].append([v, w]) 
    # graph[출발노드]에 [가중치, 도착노드]를 넣는다

def Dijkstra(start):
    weight[start]=0 # 시작노드의 가중치는 0
    heapq.heappush(heap, [0, start]) # 힙에 [가중치, 시작노드] push
    while(heap): # 힙에 원소가 없을 때까지
        w, now=heapq.heappop(heap) # 가중치가 가장 작은 값 pop
        for next_node, wei in graph[now]: # 현재 노드에 대해
            next_wei=wei+w
            # 다음노드까지의 가중치=현재 정점에서 다음 정점까지의 가중치+현재 정점까지의 가중치
            if(next_wei<weight[next_node]): 
                weight[next_node]=next_wei # 가중치 업데이트
                heapq.heappush(heap, [next_wei, next_node]) # 힙에 삽입
Dijkstra(k)
for i in range(1, V+1):
    print("{}".format(weight[i] if weight[i]!=INF else "INF"))

    