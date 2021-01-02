from itertools import combinations

height = []
for _ in range(9):
    height.append(int(input()))

for x in list(combinations(height, 7)):
    if(sum(x) == 100):
        x = list(x)
        x.sort()
        for i in x:
            print(i)
        break