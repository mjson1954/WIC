def count(x):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    idx = alpha.index(x)
    if(idx > 13):
        idx = 26 - idx
    return idx

def nextidx(name, idx, visited):
    right = 1
    left = 1
    for i in range(idx+1, len(name)):
        if(name[i] == 'A'):
            right += 1
        else:
            rightidx = i
            break
    for i in range(idx-1, idx-len(name), -1):
        if(name[i] == 'A'):
            left += 1
        else:
            leftidx = i
            break
    # print("right left ", right, left)
    if(visited[leftidx] == 0  and visited[rightidx] == 0):
        if(left < right):
            return left, leftidx, visited
        else:
            return right, rightidx, visited
    elif(visited[leftidx] == 0 and visited[rightidx] != 0):
        return left, leftidx, visited
    elif(visited[rightidx] == 0 and visited[leftidx] != 0):
        return right, rightidx, visited
    else:
        return right, rightidx, visited


def solution(name):
    answer = 0
    now = ['A' for _ in range(len(name))]
    visited = [0 for _ in range(len(name))]
    i = 0
    while(1):
        answer += count(name[i])
        now[i] = name[i]
        visited[i] = 1
        word = ''.join(now)
        # print(word)
        if(word == name):
            break
        plus, idx, visited = nextidx(name, i, visited)
        answer += plus
        i = idx
    return answer

print(solution('BBABAAAB')) # 9 되어야 한다는데..