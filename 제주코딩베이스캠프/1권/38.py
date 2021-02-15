score = list(map(int, input().split()))
score.sort(reverse=True)

print(score)
n = 1
candy = 1
now = score[0]
for i in range(1, len(score)):
    if(score[i] != now):
        n += 1
    if(n > 3):
        break
    candy += 1

print(candy)
