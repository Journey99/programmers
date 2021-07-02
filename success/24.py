# 자연수 뒤집어 배열로 만들기

def solution(n):
    return list(map(int, reversed(str(n))))

print(solution(123))


# 다른 코드

def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]