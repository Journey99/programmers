# 제일 작은 수 제거하기

def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]

print(solution([4,3,2,1]))
