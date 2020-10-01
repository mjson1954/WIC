n = int(input())
front = []
back = []
num = []
count = []

for i in range(n):
    front.append(input())
for i in range(n):
    back.append(input())

for i in range(n):
    item = back[i]
    idx = front.index(item)
    num.append(idx)

item = 0
for i in range(n):
    idx = num.index(item)
    for j in range(idx):
        if(num[j] > item and not(num[j] in count)):
                count.append(num[j])
    item += 1

print(len(count))