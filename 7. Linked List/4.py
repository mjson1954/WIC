def I(idx, value, sequence):
    sequence.insert(idx, value)
    return sequence

def D(idx, sequence):
    del sequence[idx]
    return sequence

def C(idx, value, sequence):
    sequence[idx]=value
    return sequence

T=int(input())
for test_case in range(1, T+1):
    N, M, L=map(int, input().split())
    sequence=list(map(int, input().split()))
    for i in range(M):
        form=input().split()
        if(form[0]=='I'):
            sequence=I(int(form[1]), int(form[2]), sequence)
        elif(form[0]=='D'):
            sequence=D(int(form[1]), sequence)
        else:
            sequence=C(int(form[1]), int(form[2]), sequence)
        print(i, "번째 Sequence: ", sequence)
    if(len(sequence)<=L):
        print("#{0} {1}".format(test_case, "-1"))
    else:
        print("#{0} {1}".format(test_case, sequence[L]))
