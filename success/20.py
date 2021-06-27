# x만큼 간격이 있는 숫자

def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer


# 한줄 코드

def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]