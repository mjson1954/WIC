for test_case in range(1, 11):
    T=int(input())
    array=[]
    row=0 
    column=0
    diagonal_right=0
    diagonal_left=0
    for i in range(100):
        tmp=list(map(int, input().split()))
        array.append(tmp)
        if(row<sum(tmp)):
            row=sum(tmp)
    for i in range(100):
        tmpsum=0
        for j in range(100):
            tmpsum+=array[j][i]
        if(column<tmpsum):
            column=tmpsum
    for i in range(100):
        diagonal_right+=array[i][i]
        diagonal_left+=array[99-i][i]
    print("#{0} {1}".format(test_case, max(row, column, diagonal_left, diagonal_right)))
    
    