# 정수 제곱근 판별

def solution(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

# 테스트

print(solution(121))


# import

import math

def nextSqure(n):
    # 함수를 완성하세요
    return 'no' if not math.sqrt(n).is_integer() else (math.sqrt(n)+1)**2