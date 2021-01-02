for test_case in range(1, 11):
    dump=int(input())
    box=list(map(int, input().split()))
    for i in range(dump):
        maxidx=box.index(max(box))
        minidx=box.index(min(box))
        box[maxidx]-=1
        box[minidx]+=1
    print("#{0} {1}".format(test_case, max(box)-min(box)))