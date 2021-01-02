T=int(input())
for test_case in range(1, T+1):
    N, M=map(int, input().split())
    num=input().split()
    queue=[]
    for i in range(len(num)):
        queue.append(int(num[i]))
    front=M%len(queue)
    print("#{0} {1}".format(test_case, queue[front]))
