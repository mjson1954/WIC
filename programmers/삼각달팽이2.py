def one(result, x, y, num, n):
    while(x < n and result[x][y] == 0):
        result[x][y] = num
        x += 1
        num += 1
    return result, x-1, y, num-1
    
def two(result, x, y, num, n):
    while(y < n and result[x][y] == 0):
        result[x][y] = num
        y += 1
        num += 1
    return result, x, y-1, num-1

def three(result, x, y, num, n):
    while(x >= 0 and y >= 0 and result[x][y] == 0):
        result[x][y] = num
        x -= 1
        y -= 1
        num += 1
    return result, x+1, y+1, num-1

def solution(n):
    result = [[0 for j in range(i+1)] for i in range(n)] #일단 0으로 깔기
    element = [element for array in result for element in array]
    
    x = 0
    y = 0
    num = 1
    while(0 in element):
        result, x, y, num = one(result, x, y, num, n)
        result, x, y, num = two(result, x, y+1, num+1, n)
        result, x, y, num = three(result, x-1, y-1, num+1, n)
        # print(result, x, y, num)
        x += 1
        num += 1
        element = [element for array in result for element in array]
    
    return element


print(solution(6))