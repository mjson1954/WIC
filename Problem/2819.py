T=int(input())
def fact(num):
    result=1
    temp=num
    for _ in range(num-1):
        result=result*temp
        temp-=1
    return result

def getResult(sequence):
    s=set(sequence)
    num=list(s)
    bottom=1
    if(len(num)==1):
        return 1
    else:
        for i in range(len(num)):
            bottom=bottom*fact(sequence.count(num[i]))
        return int(fact(7)/bottom)

for test_case in range(1, T+1):
    board=[]
    for _ in range(4):
        board.append(list(map(int, input().split())))
    num=[]
    sequence=[]
    for i in range(4):
        for j in range(4):
            for s in range(4):
                num.append(board[i][s])
                num.append(board[s][j])
            num.remove(board[i][j])
            num.sort()
            if(num in sequence):
                pass
            else:
                sequence.append(num)
            num=[]
    print(sequence)
    print(getResult(sequence[2]))

