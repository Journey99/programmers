# 정수 내림차순으로 정렬

def solution(n):
    return int("".join(sorted(list(str(n)), reverse = True)))