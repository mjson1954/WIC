def createQueue(n):
    s=[0 for _ in range(n)]
    front=-1
    rear=-1
def enQueue(item):
    global rear
    if isFull: print("Queue_Full")
    else:
        rear+=1
        Q[rear]=item

def deQueue(item):
    global front
    if isEmpty(): print("Queue_Empty")
    else:
        front+=1
        return Q[front]

def isEmpty():
    return front==rear

def isFull():
    return rear=len(Q)-1

def Qpeek():
    if isEmpty(): print("Queue_Empty")
    else: return Q[front+1]

