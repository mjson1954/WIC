import sys
# input = sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    n = int(input())
    new = []
    cnt = 1
    for i in range(n):
        score = list(map(int, sys.stdin.readline().strip().split()))
        new.append(score)
    new = sorted(new, key=lambda x:x[0])
    print(new)
    min = new[0][1]
    for i in range(1, n):
        if(new[i][1] < min):
            min = new[i][1]
            cnt += 1
    print(cnt)
        