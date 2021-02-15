height = list(map(int, input().split()))
original = height.copy()
height = sorted(height)
# print(height, original)
if(height == original):
    print("YES")
else:
    print("NO")