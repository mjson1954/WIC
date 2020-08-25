T = int(input())

def get_mean(money):
    return sum(money)/len(money)

for tc in range(1, T+1):
    N = int(input())
    money = list(map(int, input().split()))
    mean = get_mean(money)
    cnt = 0
    for i in range(N):
        if(money[i] <= mean):
            cnt += 1
    print("#{0} {1}".format(tc, cnt))