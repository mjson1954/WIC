def binarySearch(a, key):
    start=0
    end=len(a)-1
    while start<=end:
        middle=start+(end-start)//2
        if key==a[middle]:
            return True #검색 성공
        elif key<a[middle]:
            end=middle-1
        else:
            start=middle+1
    return False #검색 실패
