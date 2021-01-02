N=int(input())
P=list(map(int, input().split()))
P.sort()
P_sum=P
for i in range(1, len(P)):
    P_sum[i]+=P_sum[i-1]
print(sum(P_sum))