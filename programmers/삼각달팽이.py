visited = []
def plus_x(x, y, num, result, n):
    while(not([x,y] in visited) and x < n):
        result[x][y] = num
        visited.append([x,y])
        x += 1
        num += 1
        plus_x(x, y, num, result, n)
    return x, y, num, result

def plus_y(x, y, num, result, n):
    while(not([x,y] in visited) and y < n):
        result[x][y] = num
        visited.append([x,y])
        y += 1
        num += 1
        plus_y(x, y, num, result, n)
    print("plus y ", result)
    return x, y, num, result

def minus(x, y, num, result):
    while(not([x,y] in visited) and x >= 0 and y >= 0):
        result[x][y] = num
        visited.append([x,y])
        x -= 1
        y -= 1
        num += 1
        minus(x, y, num, result)
    print("minus ", result)
    return x, y, num, result

def solution(n):
    answer = []
    result = [[0 for j in range(i+1)] for i in range(n)]
    maxnum = 0
    num = 1
    for i in range(1, n+1):
        maxnum += i
    x = 0
    y = 0
    # while(num <= maxnum):
    x, y, num, result = plus_x(x, y, num, result, n)
    print("plus x ", result, x, y, num)
    x, y, num, result = plus_y(x, y, num, result, n)
    print(x, y, num)
    x, y, num, result = minus(x, y, num, result)
    print(result)
    return answer

solution(4)