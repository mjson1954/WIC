import heapq

n, m = map(int, input().split())
num = list(map(int, input().split()))
heapq.heapify(num)

for i in range(m):
    min1 = heapq.heappop(num)
    min2 = heapq.heappop(num)
    new = min1 + min2
    heapq.heappush(num, new)
    heapq.heappush(num, new)

print(sum(num))