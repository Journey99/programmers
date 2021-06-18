# 서울에서 김서방 찾기
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수

def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))
