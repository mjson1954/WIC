import heapq

n, m = map(int, input().split())
heap = [i+1 for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a_idx = heap.index(a)
    b_idx = heap.index(b)
    temp = heap[b_idx]
    heap[b_idx] = a
    heap[a_idx] = temp

#print(heap)
result = []
count = 1
while(len(result) < n):
    templist = []
    heapq.heapify(templist)
    for _ in range(count):
        if(len(heap) == 0):
            break
        temp = heap.pop(0)
        heapq.heappush(templist, temp)
    #print(templist)
    for i in range(len(templist)):
        result.append(templist[i])
    
    count = count * 2

for i in range(n):
    print(result[i], end=' ')