def solution(n, delivery):
    answer = ''
    n = ['' for i in range(n+1)]
    delivery.sort(key=lambda x:x[2], reverse=True)
    
    for i in delivery:
        # print(i)
        one = i[0]
        two = i[1] 
        if(i[2] == 1):
            n[one] = 'O'
            n[two] = 'O'
        else:
            if(n[one] == 'O'):
                n[two] = 'X'
            elif(n[two] == 'O'):
                n[one] = 'X'
            else:
                pass

    for i in range(1, len(n)):
        if(n[i] == ''):
            n[i] = '?'

    answer =''.join(n)
    return answer

n = 6
delivery = [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]

print(solution(n ,delivery))