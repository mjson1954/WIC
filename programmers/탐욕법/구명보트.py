def solution(people, limit):
    people.sort()
    temp = [0]
    #count = 0
    # while(len(people) > 0):
     #   now = people.pop()
        

    print(temp)
    answer = [item for item in temp if item != 0]
    return len(answer)

    




print(solution([40,40,40], 100))