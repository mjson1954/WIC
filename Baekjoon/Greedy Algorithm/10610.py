n=input()
num=[int(n[i]) for i in range(len(n))]
num.sort(reverse=True)
if(num[-1]!=0):
    print("-1")
else:
    if(sum(num)%3!=0):
        print("-1")
    else:
        num=map(str, num)
        print("".join(num))