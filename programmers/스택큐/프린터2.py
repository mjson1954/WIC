### 이 코드로 맞음 ###

def solution(priorities, location):
    custom = []
    printlist = []
    for i in range(len(priorities)):
        custom.append([priorities[i], i])

    while(len(custom) > 0):
        temp = custom.pop(0) # 확인해야할 요소
        flag = 1
        for i in range(len(custom)):
            if(temp[0] < custom[i][0]):
                custom.append(temp)
                flag = 0
                break
            else:
                pass
        if(flag == 1):
            printlist.append(temp)
    # print(printlist)
    result = [[i, j] for [i, j] in printlist if j==location]
    return printlist.index(result[0])+1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))