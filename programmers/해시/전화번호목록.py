def solution(phone_book):
    answer = True
    phone_book.sort()
    flag = 0
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if(phone_book[j].startswith(phone_book[i])):
                answer = False
                flag = 1
                break
        if(flag==1):
            break
            
    return answer