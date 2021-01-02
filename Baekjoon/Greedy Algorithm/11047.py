N, K=map(int, input().split())
coin=[]
count=0
for i in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
for i in range(len(coin)):
    if(K//coin[i]>0):
        count+=K//coin[i]
        K=K-coin[i]*(K//coin[i])
    if(K==0):
        break
print(count)