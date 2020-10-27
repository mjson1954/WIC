def solution(n, words):
    answer = []

    last = words[0][-1]
    for i in range(1, len(words)):
        word = words[i]
        first = word[0]
        if(word in words[:i] or last!=first):
            print(i)
            answer.append(i%n+1)
            answer.append(i//n+1)
            break
        elif(last == first):
            last = word[-1]
        else:
            pass
    if(len(answer) == 0):
        answer = [0, 0]

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))