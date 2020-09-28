x, y = map(int, input().split())
x_list = [0, x]
y_list = [0, y]
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if(a == 0):
        y_list.append(b)
    else:  
        x_list.append(b)

x_list = sorted(x_list)
y_list = sorted(y_list)
max_x = 0
max_y = 0
for i in range(len(x_list)-1):
    if(max_x < x_list[i+1]-x_list[i]):
        max_x = x_list[i+1]-x_list[i]
for i in range(len(y_list)-1):
    if(max_y < y_list[i+1]-y_list[i]):
        max_y = y_list[i+1]-y_list[i]

print(max_x * max_y)