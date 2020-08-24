n, k=map(int, input().split()) # 입력값
p=1000000007 # mod

def mul(x, y): # 거듭제곱을 계산하는 함수
    if(y==0):
        return 1
    elif(y==1):
        return x
    elif(y%2==1): # y가 홀수이면
        return mul(x, y-1)*x 
    else: # y가 짝수이면
        d=mul(x, y//2)
        d%=p # mod
        return d**2%p
t1=1 # 분자 부분이 될 n!
t2=1 # 분모 부분이 될 k!(n-k)!
for i in range(1, n+1): # n! 구하기
    t1*=i
    t1%=p
for i in range(1, k+1): # k! 구하기
    t2*=i
    t2%=p
for i in range(1, n-k+1): #(n-k)! 구하기
    t2*=i
    t2%=p
t3=mul(t2, (p-2)%p) # k!(n-k)!의 p-2 승 구하기(mod p)
# 페르마의 소정리
print((t1*t3)%p) # 결과


