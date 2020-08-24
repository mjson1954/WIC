def addtoFirst(data):
    global Head
    Head=Node(data, Head)

def add(pre, data):   #노드pre의 다음 위치에 노드 삽
    if(pre==None):
        print("error")
    else:
        pre.link=Node(data, pre.link)

def addtoLast(data): #마지막에 데이터 삽입
    global Head
    if(Head==None): #빈 리스트이면
        Head=Node(data, None)
    else:
        p=Head
        while(p.link!=None): #마지막 노드 찾을 때까지
            p=p.link
        p.link=Node(data, None)
        
def deletetoFirst(): #처음 노드 삭제
    global Head
    if(Head==None):
        print("error")
    else:
        Head=Head.link

def delete(pre): #pre 다음 노드 삭제
    if(pre==None or pre.link==None):
        print("error")
    else:
        pre.link=pre.link.link

