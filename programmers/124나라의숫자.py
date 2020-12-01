temp = []

def calc(n):
    if(n == 0):
        return
    if(n % 3 == 0):
        x = n // 3
        temp.insert(0, 4)
        calc(x-1)
    else:
        y = n % 3
        x = n//3
        temp.insert(0, y)
        if(x >= 3):
            calc(x)
        else:
            temp.insert(0, x)

def solution(n):
    calc(n)
    answer = ''
    for i in range(len(temp)):
        answer += str(temp[i])

    return str(int(answer))