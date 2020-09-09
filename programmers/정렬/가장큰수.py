def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    # num = []
    # for i in range(len(numbers)):
    #     format_num = '{0:0<4}'.format(numbers[i])
    #     num.append([numbers[i], format_num])
    # print(num)
    sorted_num = sorted(numbers, reverse=True, key=lambda number:number[0])
    print(sorted_num)
    # for i in range(len(sorted_num)-1):
    #     if(sorted_num[i][1] == sorted_num[i+1][1]):
    #         num_i = len(str(sorted_num[i][0]))
    #         num_j = len(str((sorted_num[i+1][0])))
    #         if(num_j < num_i):
    #             sorted_num[i], sorted_num[i+1] = sorted_num[i+1], sorted_num[i]

    print(sorted_num)
    for i in range(len(sorted_num)):
        if(answer == '' and sorted_num[i][0] == 0):
            pass
        else:
            answer += str(sorted_num[i][0])
    if(answer == ''):
        answer = '0'
    print(answer)
    return answer


# numbers = [6, 10, 2]
numbers = [30, 3, 34, 5, 9]
# numbers = [40, 403]
solution(numbers)


# ********삽질********
# def solution(numbers):
#     answer = ''
#     dic = {i: [] for i in range(10)}
#     numbers = list(map(str, numbers))
#     for i in range(len(numbers)):
#         dic[int(numbers[i][0])].append(numbers[i][1:])
#     print(dic)
#     idx = 9
#     for _ in range(10):
#         if(len(dic[idx]) == 1):
#             temp = str(idx) + dic[idx][0]
#             answer += temp
#         else:
#             # dic[idx] = list(sorted(dic[idx], reverse=True))
#             # print(dic[idx])
#             for i in range(len(dic[idx])-1):
#                 for j in range(i+1, len(dic[idx])):
#                     if(i == j):
#                         continue
#                     num1 = str(idx) + dic[idx][i]
#                     num2 = str(idx) + dic[idx][j]
#                 if(int(num1+num2) < int(num2+num1)):
#                     dic[idx][i], dic[idx][j] = dic[idx][j], dic[idx][i]
#             for i in range(len(dic[idx])):
#                 temp = str(idx) + dic[idx][i]
#                 answer += temp
#         idx -=1
#     print(answer)


# # numbers = [6, 10, 2]
# numbers = [30, 3, 34, 5, 9]
# # numbers = [40, 403]
# solution(numbers)