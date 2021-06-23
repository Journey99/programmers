# 두 정수 사이수 더하기

def solution(a, b):
    if a == b:
        return a
    sum = 0
    for i in range(min(a,b), max(a,b) + 1):
        sum += i
    return sum

# 다른 코드
# sum 함수를 사용하면 더 빠르게!

def adder(a, b):
    # 함수를 완성하세요
    return sum(range(min(a,b),max(a,b)+1))

