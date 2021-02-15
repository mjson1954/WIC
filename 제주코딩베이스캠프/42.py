import datetime

a = int(input())
b = int(input())

def solution(a, b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2020, a, b).weekday()]

print(solution(a, b))