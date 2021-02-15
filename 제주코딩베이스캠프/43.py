n = int(input())
binary = []

while(1):
    a = n // 2
    b = n % 2
    n = a
    binary.insert(0, b)
    if(a == 0):
        break

print(''.join(map(str, binary)))