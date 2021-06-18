# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer = [-1]
    return sorted(answer)


# 한줄코드
# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
