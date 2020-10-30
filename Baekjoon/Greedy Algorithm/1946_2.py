import sys
input = sys.stdin.readline()

T = int(input())
for _ in range(T):
    n = int(input())
    new = []
    cnt = 0
    for _ in range(n):
        score = list(map(int, input().split()))
        new.append(score)
    score.sort()
    for i in range(n):
        