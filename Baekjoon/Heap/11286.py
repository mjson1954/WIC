import heapq
import sys

input = lambda: sys.stdin.readline().strip()
# strip: 문자열의 양 끝에서 공백, 개행을 제거하는 함수

heap = []
heapq.heapify(heap)
n = int(input())
a = [int(input()) for i in range(n)]

for x in a:
    if(x == 0):
        if(len(heap)==0):
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))
        

