import sys

n = int(sys.stdin.readline().strip())
cards = set(map(int, sys.stdin.readline().split()))
print(cards)

m = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

for i in nums:
    if(i in cards):
        print(1, end=' ')
    else:
        print(0, end=' ')
