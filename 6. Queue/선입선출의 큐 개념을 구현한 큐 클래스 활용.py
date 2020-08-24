import queue
q=queue.Queue()
q.put('A')
q.put('B')

while not q.empty():
    print(q.get())
