import sys
n = int(input())

dot = []
for _ in range(n):
    dot.append(list(map(int, sys.stdin.readline().strip().split())))

dot = sorted(dot, key=lambda x: (x[0], x[1]))
# print(dot)
x = dot[0][0]
# for i in range(1, n):
#     if(dot[i][0] == x):
