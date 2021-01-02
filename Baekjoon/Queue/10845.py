import sys

input = sys.stdin.readline

n = int(input())
queue = []
for i in range(n):
    command = list(input().split())
    if(command[0] == "push"):
        queue.append(int(command[1]))
    elif(command[0] == "pop"):
        if(len(queue) > 0):
            print(queue.pop(0))
        else:
            print("-1")
    elif(command[0] == "size"):
        print(len(queue))
    elif(command[0] == "empty"):
        if(len(queue) == 0):
            print("1")
        else:
            print("0")
    elif(command[0] == "front"):
        if(len(queue) > 0):
            print(queue[0])
        else:
            print("-1")
    else:
        if(len(queue) > 0):
            print(queue[-1])
        else:
            print("-1")
