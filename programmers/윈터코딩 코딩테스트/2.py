def solution(encrypted_text, key, rotation):
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # for _ in range(rotation):
    #     answer = encrypted_text[1:]
    #     answer += encrypted_text[0]
    #     encrypted_text = answer
    n = len(encrypted_text)
    if(rotation >= 0):
        rotation = rotation % n
        answer = encrypted_text[rotation:]
        answer += encrypted_text[:rotation]
    else:
        rotation = abs(rotation)
        rotation = rotation % n
        print(rotation)
        answer = encrypted_text[rotation:]
        answer += encrypted_text[:rotation]

    print(answer)

    key = list(key)
    for i in range(len(key)):
        idx = alpha.index(key[i])
        key[i] = idx + 1

    print(key)
    answer = list(answer)
    for i in range(len(answer)):
        old = alpha.index(answer[i]) # 0
        new = old - key[i] # -1
        if(new < 0):
            new = 26 + new
        answer[i] = alpha[new]
    
    answer = ''.join(answer)
    return answer


encrypted_text = "qyyigoptvfb"
key = "abcdefghijk"
rotation = -1

print(solution(encrypted_text, key, rotation))