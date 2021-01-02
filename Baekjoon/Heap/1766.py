# 위상정렬
import heapq

n, m = map(int, input().split())
precede = [0 for _ in range(n+1)] # 위상 [0 , 1, 2, 3, 4]
rule = [[] for _ in range(n+1)]
heap = []
result = []

heapq.heapify(heap) # 위상 0인것 중 작은 것부터 출력하게

for i in range(m):
    a, b = map(int, input().split())
    rule[a].append(b) 
    precede[b] += 1

for i in range(1, n+1):
    if(precede[i] == 0):
        heapq.heappush(heap, i)

while(heap):
    num = heapq.heappop(heap)
    result.append(num)
    for i in rule[num]:
        precede[i] -=1
        if(precede[i] == 0):
            heapq.heappush(heap, i)     

print(*result) # 오 이거 좋당.