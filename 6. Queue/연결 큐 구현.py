def createLinkedQueue():
    front=None
    rear=None

def isEmpty():
    return front==None 

def enQueue(item):
    global front, rear
    newNode=Node(item)
    if isEmpty():
        front=newNode
    else:
        rear.next=newNode
    rear=newNode

def deQueue():
    global front, rear
    if isEmpty():
        print("Queue_Empty")
        return None
    item=front.item
    front=front.next
    if isEmpty():
        rear=None
    return item

def Qpeek():
    return front.item

def printQ():
    f=front
    s=""
    while f:
        s+=f.item+" "
        f=f.next
    return s

class Node:
    def __init__(self, item, n=None):
        self.item=item
        self.next=n

