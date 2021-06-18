# 문자열 다루기 기본
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성

def solution(s):
    return s.isdigit() and ( len(s) == 4 or len(s) == 6 )

print(solution("a123"))
print(solution("1234"))