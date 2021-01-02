def longest_increasing_subseq(s, MAX):
    h=[0 for i in range(MAX+1)] # s[i]로 끝나는 최장 증가 부분 수열의 길이 저장
    p=[0 for i in range(MAX+1)] # s[i] 바로 전에 나오는 원소의 인덱스 저장
    max=0 
    for i in range(1, MAX+1):
        for j in range(0, i): # 배열 h와 p를 채운다.
            if(s[i]>s[j] and h[i]<h[j]+1):
                h[i]=h[j]+1 # 길이 저장
                p[i]=j # 전 원소의 인덱스 저장
    for i in range(1, MAX+1):
        if(max<h[i]):
            max=h[i] # 최대 부분 수열의 길이 찾기
            index=i
    i=max
    lis=[] # 최대 부분 수열을 저장하는 배열
    while(index!=0): # index가 0이 될 때까지 탐색
        lis.insert(0, s[index]) # lis에 삽입
        index=p[index]
    print("최장길이:", max)
    print("최장증가부분수열:", ' '.join(map(str, lis)))

N=int(input()) # 수열의 길이
s=list(map(int, input().split())) # 수열
s.insert(0, -10000) # 0번째에 (-무한대)값으로 -10000 삽입
longest_increasing_subseq(s, N)