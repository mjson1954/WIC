def correct(p): # 올바른 괄호 문자열인가
    stack = []
    for x in p:
        if(x == '('):
            stack.append('(')
        else:
            if(len(stack) == 0):
                return False
            else:
                stack.pop()
    if(len(stack) == 0):
        return True
            
def separate(p): # u, v로 분리
    begin = 0
    end = 0
    for x in p:
        if(x == '('):
            begin += 1
        else:
            end += 1
        if(begin == end):
            break
    idx = begin + end
    return p[:idx], p[idx:]

def solution(p):
    answer = ''
    if(p == ''):
        pass
    else:
        u, v = separate(p)
        if(correct(u)):
            temp = solution(v)
            answer = u + temp
        else:
            answer += '('
            answer += solution(v)
            answer += ')'
            plus = ''
            temp = u[1:-1]
            for x in temp:
                if(x == '('):
                    plus += ')'
                else:
                    plus += '('
            answer += plus
    return answer

print(solution('()))((()'))