def solution(answers):

    pattern = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]

    result1 = [1 if an == pattern[0][i%5] else 0 for i, an in enumerate(answers)]
    result2 = [1 if an == pattern[1][i%8] else 0 for i, an in enumerate(answers)]
    result3 = [1 if an == pattern[2][i%10] else 0 for i, an in enumerate(answers)]

    score = [sum(result1), sum(result2), sum(result3)]
    maxvalue = max(score)
    answer = [i+1 for i in range(len(score))if score[i] == maxvalue]

    return answer