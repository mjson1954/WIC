def createQueue(n):
    s=[0 for _ in range(n)]
    front=0
    rear=0
def enQueue(item):
    global rear
    if isFull: print("Queue_Full")
    else:
        rear=(rear+1)%len(Q)
        Q[rear]=item

def deQueue(item):
    global front
    if isEmpty(): print("Queue_Empty")
    else:
        front=(front+1)%len(Q)
        return Q[front]
    
def delete():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front=(front+1)%len(Q)
        
def isEmpty():
    return front==rear

def isFull():
    return (rear+1)%len(Q)==front

def Qpeek():
    if isEmpty(): print("Queue_Empty")
    else: return Q[front+1]

