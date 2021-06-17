# 2016년

import datetime

def solution(a, b):
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return week[datetime.datetime(2016,a,b).weekday()]


# 테스트
print(solution(6, 23))