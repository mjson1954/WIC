from collections import deque

def differCount(one, two):
    count = 0
    for i in range(0, len(one)):
        if(one[i] != two[i]):
            count += 1
        if count > 1:
            break
    return count

def bfs(begin, target, words):
    check = [False for i in range(len(words))]
    answer = 0
    dq = deque()
    dq.appendleft(begin)

    while(len(dq) > 0):
        answer += 1
        loop = len(dq)
        for _ in range(loop):
            curWord = dq.pop()
            for i,word in enumerate(words):
                if(check[i]==False and differCount(curWord, word)==1):
                    check[i] = True
                    dq.appendleft(word)
                    if(word == target):
                        return answer
    return 0

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    print(answer)
    return answer