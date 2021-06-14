# k번째 수
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수 구하기

def solution(array, commands):
    answer = []

    for command in commands:
        new = array[command[0] - 1: command[1]]
        new.sort()
        answer.append(new[command[2] - 1])

    return answer


# 입력값 : [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# 출력값 : [5, 6, 3]

# 한줄코드

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))