def solution(s):
    answer = True
    s = s.upper()
    if s.count('P') != s.count('Y'):
        answer = False
    return answer
    # 한 줄로 풀어보기(도전)
    # if s.upper().count('P') != s.upper().count('Y'):
    #     return False
    # else:
    #     return True
    # 한 줄로 풀어보기(해설)
    # return s.lower().count('p') == s.lower().count('y')