from itertools import combinations

a = ["a", "e", "i", "o", "u"]


L, C = map(int, input().split())
char = list(input().split())

char.sort()
for x in list(combinations(char, L)):
    count_a = 0
    count_b = 0
    for i in x:
        if i in a:
            count_a += 1
        else:
            count_b += 1
    if(count_a >= 1 and count_b >= 2):
        answer = ''.join(x)
        print(answer)
        

    