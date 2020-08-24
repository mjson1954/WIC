def is_there(list, x):
    for i in range(len(list)):
        if(x==list[i]):
            return i
    return 0

a=[1, 3, 5]
print(is_there(a, 3))
