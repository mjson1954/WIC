data = list(input().split())
dataset = list(set(data))
max = 0
name = ''
for i in range(len(dataset)):
    n = data.count(dataset[i])
    if(n > max):
        max = n
        name = dataset[i]

print("{0}(이)가 총 {1}표로 반장이 되었습니다.".format(name, max))
