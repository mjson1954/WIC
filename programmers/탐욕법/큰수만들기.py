def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while(len(stack) > 0 and stack[-1] < num and k > 0):
            k -= 1
            stack.pop()
        stack.append(num)
    if(k != 0):
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer

print(solution('9999999', 4))
print(solution('4177252841', 4))