data = input()

for x in data:
    if(x.upper() == x): # 대문자이면
        print(x.lower(), end='')
    else:
        print(x.upper(), end='')

