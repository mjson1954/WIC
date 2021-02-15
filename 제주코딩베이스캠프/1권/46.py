result = 0
for i in range(1, 101):
    num = str(i)
    for n in num:
        result += int(n)

print(result)
