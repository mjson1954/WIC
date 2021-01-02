def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        index = []
        flag = 0
        for alpha in skill_trees[i]:
            if(alpha in skill):
                idx = skill.index(alpha)
                if(len(index)==0 and idx==0):
                    index.append(idx)
                elif(len(index)==0 and idx!=0):
                    flag = 1
                    break
                else:
                    if(max(index) + 1 == idx): # 작아야함
                        index.append(idx)
                    else:
                        flag = 1
                        break
            if(flag == 1):
                break
        if(flag == 0):
            answer += 1

    return answer


skill = "CBD"
# C, CB, CD, CBD
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))