# 가운데 글자 가져오기

def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[len(s)//2 - 1:len(s)//2 +1]
    else:
        answer = s[len(s) //2]

    return answer

# 테스트
# print(solution("qwer"))


# if 안쓰고 한줄코드

def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]


