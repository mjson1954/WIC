name = list(input().split())
score = list(map(int, input().split()))

dic = dict(zip(name, score))
print(dic)