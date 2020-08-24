girl, boy, internship=map(int, input().split())
maxteam=0
for i in range(internship+1):
    girl_tmp=girl-i
    boy_tmp=boy-(internship-i)
    if(girl_tmp//2<boy_tmp):
        maxtmp=girl_tmp//2
    else:
        maxtmp=boy_tmp
    if(maxtmp>maxteam):
        maxteam=maxtmp
print(maxteam)