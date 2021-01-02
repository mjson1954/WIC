def solution(clothes):
    answer = 1
    clothes_dic = {}
    for i in range(len(clothes)):
        if(clothes[i][1] in clothes_dic.keys()):
            clothes_dic[clothes[i][1]].append(clothes[i][0])
        else:
            clothes_dic[clothes[i][1]] = [clothes[i][0]]

    clothes_key = list(clothes_dic.keys())
    for i in range(len(clothes_dic)):
        key = clothes_key[i]
        answer = answer * (len(clothes_dic[key]) + 1)

    return answer-1

# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# print(solution(clothes))