# 하샤드 수

def solution(x):
    sum = 0

    for i in str(x):
        sum += int(i)

    if x % sum == 0:
        return True
    else:
        return False


# 테스트
print(solution(12))



# 다른 한줄 코드
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0